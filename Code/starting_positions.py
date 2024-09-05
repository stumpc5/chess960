import random

def StartingPosition(at_random=True):
    """
    Generate a Chess960 starting position with pieces placed on the first rank.

    Args:
        at_random (bool): If True, generates a random Chess960 starting position. 
                          If False, returns the standard chess starting position.

    Returns:
        str: A string representing the starting position of pieces on the first rank.
    """
    if at_random:
        # Initialize an empty board (None represents an empty square)
        start_pos = [None] * 8

        # Place the black-squared bishop on an even index (0, 2, 4, 6)
        black_bishop_index = random.choice([0, 2, 4, 6])
        start_pos[black_bishop_index] = "b"

        # Place the white-squared bishop on an odd index (1, 3, 5, 7)
        white_bishop_index = random.choice([1, 3, 5, 7])
        start_pos[white_bishop_index] = "b"

        # Place the two knights
        knight_indices = random.sample([i for i in range(8) if start_pos[i] is None], 2)
        start_pos[knight_indices[0]] = "n"
        start_pos[knight_indices[1]] = "n"

        # Place the queen
        queen_index = random.choice([i for i in range(8) if start_pos[i] is None])
        start_pos[queen_index] = "q"

        # Place the rooks and the king, ensuring rooks are on either side of the king
        empty_indices = [i for i in range(8) if start_pos[i] is None]
        rook1_index, king_index, rook2_index = sorted(empty_indices)  # Sort to ensure proper rook-king-rook sequence
        start_pos[rook1_index] = "r"
        start_pos[king_index] = "k"
        start_pos[rook2_index] = "r"

        # Join the list into a string representing the starting position
        start_pos_str = "".join(start_pos)
    else:
        # Standard chess starting position
        start_pos_str = "rnbqkbnr"

    return start_pos_str

def AllStartingPositions():
    """
    Generate all 960 possible starting positions for Chess960.

    Too lazy to make this more efficient.

    Returns:
        List[str]: A sorted list of all unique Chess960 starting positions.
    """
    positions = set()

    # Generate positions until we have all 960 unique Chess960 configurations
    while len(positions) < 960:
        positions.add(StartingPosition(at_random=True))
    
    return sorted(positions)
