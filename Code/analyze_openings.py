import time
import json
import os
import argparse
import cProfile
import pstats
from read_pgn           import ReadPGN
from starting_positions import AllStartingPositions, GetChess960Index
from identify_openings  import IdentifyOpenings
from markdown_templates import header_template, openings_template, opening_template, board_template
from concurrent.futures import ProcessPoolExecutor, as_completed


# Load configuration from configuration.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'configuration.json')
with open(CONFIG_PATH, 'r') as config_file:
    config = json.load(config_file)

DATAFOLDER           = config["DATAFOLDER"]
MARKDOWN_BASE_FOLDER = config["MARKDOWN_BASE_FOLDER"]
MARKDOWN_FOLDER      = MARKDOWN_BASE_FOLDER + config["MARKDOWN_FOLDER"]
OVERVIEW_FILE        = MARKDOWN_BASE_FOLDER + config["OVERVIEW_FILE"]
OVERVIEW_TEMPLATE    = config["OVERVIEW_TEMPLATE"]
THRESHOLDS           = config["THRESHOLDS"]
MAX_SIZE             = config["MAX_SIZE"]
FILENAME_TEMPLATE    = config["FILENAME_TEMPLATE"]
N_WORKERS            = config.get("N_WORKERS", None)

def GenerateOpeningTable(board="rnbqkbnr", thresholds=THRESHOLDS, verbose=True, max_size=MAX_SIZE, datafolder=DATAFOLDER, filename_template=FILENAME_TEMPLATE):
    """
    Generates a table of chess openings based on the board position and thresholds provided.

    Args:
        board (str): The FEN string representing the board position. Defaults to the standard start position.
        thresholds (list of float): A list of thresholds to filter openings.
        max_size (int): Maximum number of games to read from PGN. Defaults to MAX_SIZE.
        datafolder (str): Path to the folder containing the compressed PGN data.

    Returns:
        tuple: A tuple containing statistics and an openings table for each threshold.
    """
    games = ReadPGN(board, folder=datafolder, filename_template=filename_template, max_size=max_size, verbose=verbose)

    openings_table = dict()

    for threshold in thresholds:
        stats, openings = IdentifyOpenings(games, threshold)
        openings_table[threshold] = openings

    avg_nr_moves = round(sum(int(game[2]) for game in games) / len(games))
    avg_wall_time = round(sum(float(game[3][:-4]) for game in games) / len(games), 1)
    return stats, openings_table, avg_nr_moves, avg_wall_time

def GenerateBoardMarkdown(board="rnbqkbnr", thresholds=THRESHOLDS, verbose=True, save_result=False, max_size=MAX_SIZE):
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
    index = GetChess960Index(board)
    stats, opening_tables, avg_nr_moves, avg_wall_time = GenerateOpeningTable(board=board, thresholds=thresholds, verbose=verbose, max_size=max_size)

    # formating the header
    nr_games, (percent_white, percent_draw, percent_black) = stats

    header_data = {
        'board'         : board.upper(),
        'index'         : index,
        'nr_games'      : nr_games,
        'time_moves'    : f"{avg_wall_time} secs for {avg_nr_moves} moves",
        'percent_white' : ToPer(percent_white),
        'percent_draw'  : ToPer(percent_draw),
        'percent_black' : ToPer(percent_black),
        'points'        : ToPer(percent_white + percent_draw/2, absolute=True),
    }
    content = header_template.format(**header_data)

    #formating each opening and append it to the opening header
    for threshold in reversed(sorted(opening_tables)):
        openings = opening_tables[threshold]

        #formating the opening heading
        threshold_data = {
            'threshold' : ToPer(threshold)
        }
        openings_header = openings_template.format(**threshold_data)

        openings = sorted(openings, key = lambda opening: -sum(move[1][0] for move in opening[1]))

        for opening, moves in openings:
            opening_prob = sum(move[1][0] for move in moves)
            moves       = moves[:5]
            opening_data = {
                'opening'       : AlgebraicNotation(opening),
                'opening_prob'  : ToPer(opening_prob),
                'moves'         : " <p> ".join(move for move,_ in moves),
                'move_prob'     : " <p> ".join(ToPer(prob) for _,(prob,_) in moves),
                'percent_white' : " <p> ".join(ToPer(per[0]) for _,(_,per) in moves),
                'percent_draw'  : " <p> ".join(ToPer(per[1]) for _,(_,per) in moves),
                'percent_black' : " <p> ".join(ToPer(per[2]) for _,(_,per) in moves),
                'points'        : " <p> ".join(ToPer(per[0] + per[1]/2, absolute=True) for _,(_,per) in moves),
            }
            opening_tmp = opening_template.format(**opening_data)
            openings_header += opening_tmp + "\n"
        content += "\n\n" + openings_header

    if save_result:
        with open(MARKDOWN_FOLDER + f'/{board}.md', 'w') as file:
            file.write(content)
        return stats
    else:
        return content

def analyze_and_write_board(board, max_size):
    try:
        stats = GenerateBoardMarkdown(board=board, thresholds=THRESHOLDS, verbose=False, save_result=True, max_size=max_size)
        nr_games, (percent_white, percent_draw, percent_black) = stats
        return {
            'board': board,
            'nr_games': nr_games,
            'percent_white': percent_white,
            'percent_draw': percent_draw,
            'percent_black': percent_black,
            'points': percent_white + percent_draw/2,
        }
    except FileNotFoundError:
        print(f"                  ERROR: no pgn's found for board { board.upper() }")
        return {
            'board': board,
            'nr_games': 0,
            'percent_white': 0.0,
            'percent_draw': 0.0,
            'percent_black': 0.0,
            'points': 0.0,
        }

def GenerateAllMarkdown(boards=None, thresholds=THRESHOLDS, verbose=True, max_size=MAX_SIZE):
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

    results = []
    with ProcessPoolExecutor(max_workers=N_WORKERS) as executor:
        future_to_board = {executor.submit(analyze_and_write_board, board, max_size): board for board in boards}
        for i, future in enumerate(as_completed(future_to_board)):
            board = future_to_board[future]
            try:
                result = future.result()
                board_datas.append( {
                    'board_index'   : GetChess960Index(board),
                    'board_name'    : board.upper(),
                    'board_link'    : config["MARKDOWN_FOLDER"] + board,
                    'nr_games'      : result['nr_games'],
                    'percent_white' : ToPer(result['percent_white']),
                    'percent_draw'  : ToPer(result['percent_draw']),
                    'percent_black' : ToPer(result['percent_black']),
                    'points'        : ToPer(result['points'], absolute=True),
                } )
                readme_boards.append(board_template.format(**board_datas[-1]))
            except Exception as e:
                print(f"ERROR processing board {board}: {e}")
            if verbose:
                elapsed_time = time.time() - start_time
                print(f"{ i+1 }/{ len(boards) } (time: {elapsed_time:.1f} sec): Generated { board.upper() } with { board_datas[-1]['nr_games'] if board_datas else 0 } games")

    # After collecting all board_datas, sort them by SPI (index in boards)
    board_order = {board.upper(): i for i, board in enumerate(boards)}
    board_datas.sort(key=lambda d: board_order[d['board_name']])

    # writing the data in the order given by advantage for white
    readme_boards_sorted = []
    for board_data in sorted(board_datas, key=lambda D: -float(D['points'])):
        readme_boards_sorted.append(board_template.format(**board_data))

    readme = readme_template % ("\n".join(board_template.format(**d) for d in board_datas), "\n".join(readme_boards_sorted))

    with open(OVERVIEW_FILE, 'w') as file:
        file.write(readme)

def ToPer(x, absolute=False):
    """
    Floating-point value to percentage string formatted to one decimal place.
    """
    if absolute is False:
        return f"{100*x:.1f}%"
    else:
        return f"{x:.3f}"

def AlgebraicNotation(opening):
    result = ""
    for idx, move in enumerate(opening):
        if idx % 2 == 0:
            result += f" {1 + idx//2}.{move}"
        else:
            result += f" {move}"
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chess960 Opening Analysis")
    parser.add_argument('--board', type=str, help='FEN string for the board to analyze (default: all boards)')
    parser.add_argument('--max_size', type=int, help='Maximum number of games to read from PGN (overrides config)')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--profile', action='store_true', help='Enable cProfile profiling')
    args = parser.parse_args()

    # Override config if arguments are provided
    max_size = args.max_size if args.max_size is not None else MAX_SIZE
    verbose  = args.verbose
    boards    = [args.board.lower()] if args.board else None

    def run_main():
        GenerateAllMarkdown(boards=boards, verbose=verbose, max_size=max_size)

    if args.profile:
        profile_file = 'profile_output.prof'
        cProfile.run('run_main()', profile_file)
        print(f"Profiling complete. Stats written to {profile_file}.")
        stats = pstats.Stats(profile_file)
        stats.sort_stats('cumulative').print_stats(30)
    else:
        run_main()
