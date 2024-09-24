import re
import io
import os
import tarfile
import chess.pgn

DATAFOLDER = "../../Data960/"

def ReadPGN(board, folder=DATAFOLDER, max_size=float('inf'), verbose=False):
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
    filename = f"data_{board}_new.pgn"
    tar_path = os.path.join(folder, f"{filename}.tar.gz")

    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Archive {tar_path} not found.")

    try:
        with tarfile.open(tar_path, "r:gz") as tar:
            fileobj = tar.extractfile(filename)
            if fileobj is None:
                raise FileNotFoundError(f"File {filename} not found inside the archive.")
            game = []
            empty_line_count = 0
            for line in fileobj:
                line = line.decode('utf-8').strip()
                if line == "":
                    empty_line_count += 1
                    if empty_line_count % 2 == 0:
                        moves, res = ParseGame("\n".join(game))

                        if res == "1-0":
                            res = 1.0
                        elif res == "1/2-1/2":
                            res = 0.5
                        elif res == "0-1":
                            res = 0.0
                        else:
                            raise ValueError(f"Unrecognized result: {result}")

                        games.append((moves, res))
                        game = []
                        if len(games) == max_size:
                            break
                        empty_line_count = False
                    else:
                        empty_line_count = True
                game.append(line)
        if verbose:
            print(f"Total games processed for board '{board}': {len(games)}")
        return games

    except tarfile.TarError as e:
        raise RuntimeError(f"Error processing tar archive: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error occurred: {str(e)}")

def ParseGame(game):
    meta, game = game.split("\n\n")
    game = " ".join(game.splitlines())
    game = re.sub(r'\{.*?\}', '', game)
    game = re.sub(r'\d+\.\.\.', '', game).strip()
    game = re.sub(r'\s+', ' ', game)
    game = re.sub(r'\d+\.\s*', '', game)

    game = game.split(" ")
    res = game[-1]
    game = game[:-1]
    assert res in ["0-1", "1/2-1/2", "1-0"]

    return game, res
