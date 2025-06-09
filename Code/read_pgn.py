import re
import io
import os
import tarfile
import chess.pgn

def ReadPGN(board, folder, filename_template, max_size=float('inf'), verbose=False):
    """
    Reads chess games from a compressed PGN file within a .tar.gz archive and extracts the moves and results.

    Args:
        board (str)    : The starting board (used as part of the PGN filename).
        folder (str)   : The directory containing the .tar.gz archive (default is "../Data960/").
        max_size (int) : Maximum number of games to read (default is unlimited).

    Returns:
        List[Tuple[Tuple[str], float]]: A list of tuples where each tuple contains the moves as strings and the game result as a float.
    """

    games = []
    filename = filename_template.format(board)
    tar_path = os.path.abspath(os.path.join(folder, f"{filename}.tar.gz"))

    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Archive {tar_path} not found.")

    try:
        with tarfile.open(tar_path, "r:gz") as tar:
            fileobj = tar.extractfile(filename)
            if fileobj is None:
                raise FileNotFoundError(f"File {filename} not found inside the archive.")
            # Read and decode the entire file at once
            content = fileobj.read().decode('utf-8')
            # Split games by two or more newlines followed by a header (robust PGN split)
            raw_games = [g for g in re.split(r'\n\s*\n(?=\[)', content) if g.strip()]
            for raw_game in raw_games:
                try:
                    moves, res, (nr_moves, wall_time) = ParseGame(raw_game)
                    if res == "1-0":
                        res = 1.0
                    elif res == "1/2-1/2":
                        res = 0.5
                    elif res == "0-1":
                        res = 0.0
                    else:
                        raise ValueError(f"Unrecognized result: {res}")
                    games.append((moves, res, nr_moves, wall_time))
                    if len(games) == max_size:
                        break
                except Exception as e:
                    if verbose:
                        print(f"Skipping game due to error: {e}")
        if verbose:
            print(f"Total games processed for board '{board}': {len(games)}")
        return games

    except tarfile.TarError as e:
        raise RuntimeError(f"Error processing tar archive: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error occurred: {str(e)}")

# Pre-compile regex patterns for performance
RE_COMMENT = re.compile(r'\{.*?\}')
RE_MOVE_NUM_AND_DOTS = re.compile(r'\d+\.(?:\.\.)?\s*')
RE_WHITESPACE = re.compile(r'\s+')

def ParseGame(game):
    # Split only on the first double newline to separate meta and moves
    meta, moves_section = game.split("\n\n", 1)
    moves = " ".join(moves_section.splitlines())
    # Only call regex if needed
    if '{' in moves:
        moves = RE_COMMENT.sub('', moves)
    moves = RE_MOVE_NUM_AND_DOTS.sub('', moves)
    moves = RE_WHITESPACE.sub(' ', moves).strip()

    # Get result and moves efficiently
    if ' ' in moves:
        moves, res = moves.rsplit(' ', 1)
        moves = moves.split(' ')
    else:
        raise ValueError("No moves found")

    if res not in ["0-1", "1/2-1/2", "1-0"]:
        print(moves)
        print(meta)
        raise ValueError(f"Unrecognized result: {res}")

    nr_moves = wall_time = None
    for l in meta.splitlines():
        if l.startswith("[NrMoves"):
            nr_moves = l.split('"')[1]
        if l.startswith("[WallTime"):
            wall_time = l.split('"')[1]

    assert res in ["0-1", "1/2-1/2", "1-0"]

    return moves, res, (nr_moves, wall_time)