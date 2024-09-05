import time
from read_pgn           import ReadPGN
from starting_positions import AllStartingPositions
from identify_openings  import IdentifyOpenings
from markdown_templates import header_template, openings_template, opening_template, board_template

MARKDOWN_FOLDER = "../BoardAnalysis"

def GenerateOpeningTable(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True):
    matches = ReadPGN(board, max_size=200000, verbose=verbose)

    openings_table = dict()
    winning  = 0

    for threshold in thresholds:
        stats, openings = IdentifyOpenings(matches, threshold)
        openings_table[threshold] = openings

    return stats, openings_table

def GenerateBoardMarkdown(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True, save_result=False):
    stats, opening_tables = GenerateOpeningTable(board=board, thresholds=thresholds, verbose=verbose)

    # formating the header
    nr_matches, (percent_white, percent_draw, percent_black) = stats
    header_data = {
        'board'         : board.upper(),
        'nr_matches'    : nr_matches,
        'percent_white' : ToPer(percent_white),
        'percent_draw'  : ToPer(percent_draw),
        'percent_black' : ToPer(percent_black),
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
            min_prob = moves[0][1][0] / 3
            moves = [ move for move in moves if move[1][0] >= min_prob ]
            opening_data = {
                # old separator &rarr; 
                'opening'       : " ".join(opening),
                'moves'         : " <p> ".join(move for move,_ in moves),
                'move_prob'     : " <p> ".join(ToPer(prob) for _,(prob,_) in moves),
                'percent_white' : " <p> ".join(ToPer(per[0]) for _,(_,per) in moves),
                'percent_draw'  : " <p> ".join(ToPer(per[1]) for _,(_,per) in moves),
                'percent_black' : " <p> ".join(ToPer(per[2]) for _,(_,per) in moves),
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
    if boards is None:
        boards = AllStartingPositions()

    readme_boards = []

    start_time = time.time()

    for i, board in enumerate(boards):
        if verbose:
            elapsed_time = time.time() - start_time
            print(f"{ i+1 }/{ len(boards) } (time: {elapsed_time:.1f} sec): Generating { board.upper() }")

        try:
            stats = GenerateBoardMarkdown(board=board, thresholds=thresholds, verbose=False, save_result=True)
        except FileNotFoundError:
            print(f"                  ERROR: no pgn's found for board { board.upper() }")
            pass
        else:
            nr_matches, (percent_white, percent_draw, percent_black) = stats
            board_data = {
                'board_name'    : board.upper(),
                'board_link'    : board,
                'nr_matches'    : nr_matches,
                'percent_white' : ToPer(percent_white),
                'percent_draw'  : ToPer(percent_draw),
                'percent_black' : ToPer(percent_black),
            }
            readme_boards.append(board_template.format(**board_data))

            with open('../readme_template.md', 'r') as file:
                readme_template = file.read()
            readme = readme_template % "\n".join(readme_boards)

            with open('../README_ANALYSIS.md', 'w') as file:
                file.write(readme)

def ToPer(x):
    return str(round(x*1000)/10) + "%"
