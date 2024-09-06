import time
from read_pgn           import ReadPGN
from starting_positions import AllStartingPositions
from identify_openings  import IdentifyOpenings
from markdown_templates import header_template, openings_template, opening_template, board_template

MARKDOWN_FOLDER   = "../BoardAnalysis"
OVERVIEW_FILE     = "../analysis_overview.md"
OVERVIEW_TEMPLATE = "templates/overview_template.md"

def GenerateOpeningTable(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True):
    """
    Generates a table of chess openings based on the board position and thresholds provided.

    Args:
        board (str): The FEN string representing the board position. Defaults to the standard start position.
        thresholds (list of float): A list of thresholds to filter openings.

    Returns:
        tuple: A tuple containing statistics and an openings table for each threshold.
    """
    matches = ReadPGN(board, max_size=50000, verbose=verbose)

    openings_table = dict()
    winning  = 0

    for threshold in thresholds:
        stats, openings = IdentifyOpenings(matches, threshold)
        openings_table[threshold] = openings

    return stats, openings_table

def GenerateBoardMarkdown(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True, save_result=False):
    """
    Generates markdown content summarizing the analysis of chess openings for a specific board position.

    Args:
        board (str): The FEN string representing the board position.
        thresholds (list of float): A list of thresholds to filter openings.
        save_result (bool): If True, saves the result to a markdown file.

    Returns:
        str or tuple: If save_result is False, returns the markdown content. 
                      If save_result is True, returns the analysis statistics.
    """
    stats, opening_tables = GenerateOpeningTable(board=board, thresholds=thresholds, verbose=verbose)

    # formating the header
    nr_matches, (percent_white, percent_draw, percent_black) = stats
    header_data = {
        'board'         : board.upper(),
        'nr_matches'    : nr_matches,
        'percent_white' : ToPer(percent_white),
        'percent_draw'  : ToPer(percent_draw),
        'percent_black' : ToPer(percent_black),
        'points'        : ToPer(percent_white + percent_draw/2)[:-1],
    }
    header = header_template.format(**header_data)

    #formating each opening and append it to the opening header
    for threshold in reversed(sorted(opening_tables)):
        openings = opening_tables[threshold]

        #formating the opening heading
        threshold_data = {
            'threshold' : ToPer(threshold)
        }
        openings_header = openings_template.format(**threshold_data)

        for opening, moves in openings:
            if moves:
                min_prob = moves[0][1][0] / 3
            else:
                min_prob = 0
            moves = [ move for move in moves if move[1][0] >= min_prob ]
            opening_data = {
                # old separator &rarr; 
                'opening'       : " ".join(opening),
                'moves'         : " <p> ".join(move for move,_ in moves),
                'move_prob'     : " <p> ".join(ToPer(prob) for _,(prob,_) in moves),
                'percent_white' : " <p> ".join(ToPer(per[0]) for _,(_,per) in moves),
                'percent_draw'  : " <p> ".join(ToPer(per[1]) for _,(_,per) in moves),
                'percent_black' : " <p> ".join(ToPer(per[2]) for _,(_,per) in moves),
                'points'        : " <p> ".join(ToPer(per[0] + per[1]/2)[:-1] for _,(_,per) in moves),
            }
            opening_tmp = opening_template.format(**opening_data)
            openings_header += opening_tmp + "\n"
        header += "\n\n" + openings_header

    if save_result:
        with open(MARKDOWN_FOLDER + f'/{ board }.md', 'w') as file:
            file.write(header)
        return stats
    else:
        return header

def GenerateAllMarkdown(boards=None, thresholds=[0.01, 0.02, 0.05], verbose=True):
    """
    Generates markdown files for all board positions or a list of specific board positions.

    Args:
        boards (list of str): A list of FEN strings representing the board positions.
                              If None, generates for all starting positions.
        thresholds (list of float): A list of thresholds to filter openings.
    """
    if boards is None:
        boards = AllStartingPositions()

    readme_boards = []
    board_datas   = []

    with open(OVERVIEW_TEMPLATE, 'r') as file:
        readme_template = file.read()

    start_time = time.time()

    for i, board in enumerate(boards):
        try:
            stats = GenerateBoardMarkdown(board=board, thresholds=thresholds, verbose=False, save_result=True)
        except FileNotFoundError:
            print(f"                  ERROR: no pgn's found for board { board.upper() }")
            pass
            nr_matches = 0
        else:
            nr_matches, (percent_white, percent_draw, percent_black) = stats
            board_datas.append( {
                'board_index'   : i+1,
                'board_name'    : board.upper(),
                'board_link'    : board,
                'nr_matches'    : nr_matches,
                'percent_white' : ToPer(percent_white),
                'percent_draw'  : ToPer(percent_draw),
                'percent_black' : ToPer(percent_black),
                'points'        : ToPer(percent_white + percent_draw/2)[:-1],
            } )
            readme_boards.append(board_template.format(**board_datas[-1]))

            # writing the data again in the order given by advantage for white
            readme_boards_sorted = []
            for board_data in sorted(board_datas, key=lambda D: -float(D['points'])):
                readme_boards_sorted.append(board_template.format(**board_data))

            readme = readme_template % ("\n".join(readme_boards), "\n".join(readme_boards_sorted))

            with open(OVERVIEW_FILE, 'w') as file:
                file.write(readme)
        if verbose:
            elapsed_time = time.time() - start_time
            print(f"{ i+1 }/{ len(boards) } (time: {elapsed_time:.1f} sec): Generated { board.upper() } with { nr_matches } matches")

def ToPer(x):
    """
    Floating-point value to percentage string formatted to one decimal place.
    """
    return str(round(x*1000)/10) + "%"
