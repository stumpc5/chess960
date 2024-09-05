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
    filename = f"data_{board}.pgn"
    tar_path = os.path.join(folder, f"{filename}.tar.gz")

    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Archive {tar_path} not found.")

    try:
        with tarfile.open(tar_path, "r:gz") as tar:
            fileobj = tar.extractfile(filename)
            if fileobj is None:
                raise FileNotFoundError(f"File {filename} not found inside the archive.")
            
            pgn = io.TextIOWrapper(fileobj, encoding='utf-8')
            
            while len(games) < max_size:
                game = chess.pgn.read_game(pgn)
                if game is None:
                    break  # No more games to read
                
                moves = tuple(str(move) for move in game.mainline_moves())
                result = game.headers.get("Result", "Unknown").split("-")[0]

                if result == "1":
                    result = 1.0
                elif result == "1/2":
                    result = 0.5
                elif result == "0":
                    result = 0.0
                else:
                    raise ValueError(f"Unrecognized result: {result}")

                games.append((moves, result))
        if verbose:
            print(f"Total games processed for board '{board}': {len(games)}")
        return games

    except tarfile.TarError as e:
        raise RuntimeError(f"Error processing tar archive: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error occurred: {str(e)}")
