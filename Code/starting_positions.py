import random

def AllStartingPositions():
    """
    Generate all 960 possible starting positions for Chess960.

    Returns:
        List[str]: A sorted list of all unique Chess960 starting positions.
    """
    return [ Chess960StartingPosition(N) for N in range(960) ]

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
        
        return Chess960StartingPosition(random.randint(0,959))
    else:
        # Standard chess starting position
        return "rnbqkbnr"

# The following was completely written by ChatGPT (immediately at first prompt)
def Chess960StartingPosition(N):
    # Step a: Place the first bishop on a bright square (b, d, f, h)
    bright_squares = ['b', 'd', 'f', 'h']
    B1 = N % 4
    first_bishop = bright_squares[B1]
    N2 = N // 4

    # Step b: Place the second bishop on a dark square (a, c, e, g)
    dark_squares = ['a', 'c', 'e', 'g']
    B2 = N2 % 4
    second_bishop = dark_squares[B2]
    N3 = N2 // 4

    # Step c: Place the queen on one of the remaining squares
    remaining_squares = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    remaining_squares.remove(first_bishop)
    remaining_squares.remove(second_bishop)
    
    Q = N3 % 6
    queen = remaining_squares[Q]
    remaining_squares.remove(queen)
    N4 = N3 // 6

    # Step d: Place the knights based on N4 using the table
    knight_positions = [
        [0, 1], [0, 2], [0, 3], [0, 4], [1, 2], 
        [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
    ]
    knight_indices = knight_positions[N4]
    knights = [remaining_squares[knight_indices[0]], remaining_squares[knight_indices[1]]]

    # Remove knight squares from remaining squares
    knight1 = remaining_squares.pop(knight_indices[0])
    knight2 = remaining_squares.pop(knight_indices[1] - 1)  # second index adjusts after first removal

    # Step e: Place the rooks and king
    rook1 = remaining_squares[0]
    king = remaining_squares[1]
    rook2 = remaining_squares[2]

    # Combine all pieces to form the final starting position
    pieces_order = {
        first_bishop: 'b',
        second_bishop: 'b',
        queen: 'q',
        knight1: 'n',
        knight2: 'n',
        rook1: 'r',
        king: 'k',
        rook2: 'r'
    }

    final_position = ''.join([pieces_order[square] for square in 'abcdefgh'])
    
    return final_position
