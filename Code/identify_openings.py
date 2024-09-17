def IdentifyOpenings(games, threshold):
    """
    Identifies the most common chess openings in a list of games and calculates the percentages of white wins, draws, and black wins after those openings.

    An opening is included if the percentages of games starting with this opening is at least the threshold, while adding any additional step drops below the threshold.

    Args:
        games (List[Tuple[Tuple[str], float]]): A list of tuples where each tuple contains the moves as strings and the game result as a float.
        threshold (float): A value between 0 and 1 representing the minimum percentage of games that should start with a specific opening.

    Returns:
        Tuple:
            - (int, Tuple[float, float, float]): A tuple containing:
                - The total number of games.
                - The percentage of white wins, draws, and black wins overall.
            - List[Tuple[List[str], Tuple[float, float, float]]]: A list of tuples where each tuple contains:
                - A list of moves representing the opening.
                - A tuple with the percentage of white wins, draws, and black wins after that opening.
    """
    if not (0 <= threshold <= 1):
        raise ValueError("Threshold must be between 0 and 1")

    openings = []
    to_test = [[]]  # Sequences of moves to test

    # Build possible openings based on the game data
    while to_test:
        current_opening = to_test.pop()
        next_steps = BetterOpenings(games, [step for step, _ in current_opening])

        new_openings = [
            current_opening + [(step, (white, draw, black))]
            for step, (count, (white, draw, black)) in next_steps
            if count > threshold
        ]

        if not new_openings:
            # No further expansion is possible, so finalize this opening
            openings.append(([step for step, _ in current_opening], next_steps))
        else:
            to_test.extend(new_openings)

    # Calculate overall win percentages for white, draws, and black
    nr_games = len(games)
    if nr_games == 0:
        raise ValueError("No games provided")

    white_wins = sum(1 for _, result in games if result == 1.0) / nr_games
    draws      = sum(1 for _, result in games if result == 0.5) / nr_games
    black_wins = sum(1 for _, result in games if result == 0.0) / nr_games

    winning_summary = (nr_games, (white_wins, draws, black_wins))

    return winning_summary, openings

def BetterOpenings(games, opening):
    """
    Finds potential next moves in games that extend a given opening sequence and calculates win percentages after those moves.

    Args:
        games (List[Tuple[Tuple[str], float]]): A list of tuples where each tuple contains the moves as strings and the game result as a float.
        opening (List[str]): A prefix (sequence of moves) to look for in the games.

    Returns:
        List[Tuple[str, Tuple[float, Tuple[float, float, float]]]]: A list of tuples where each tuple contains:
            - The next move that can extend the opening.
            - A tuple with:
                - The percentage of total games that continue with this move.
                - A tuple of the percentage of white wins, draws, and black wins after this move.
    """
    next_steps: Dict[str, Tuple[int, Tuple[int, int, int]]] = {}
    opening_length = len(opening)

    for game, result in games:
        if opening_length < len(game):
            for i in range(opening_length):
                if game[i] != opening[i]:
                    break
            else:
                # Found a game for the opening prefix
                next_move = game[opening_length]
                count, (white, draw, black) = next_steps.get(next_move, (0, (0, 0, 0)))
                count += 1

                # Update result counts
                if result == 1.0:
                    white += 1
                elif result == 0.5:
                    draw += 1
                elif result == 0.0:
                    black += 1
                else:
                    raise ValueError(f"Unrecognized game result: {result}")

                next_steps[next_move] = (count, (white, draw, black))

    total_games = len(games)

    # Calculate the percentages of white wins, draws, and black wins for each next move
    next_steps = [
        (move, (count / total_games, (white / count, draw / count, black / count)))
        for move, (count, (white, draw, black)) in next_steps.items()
        if count > 0
    ]
    next_steps = sorted(next_steps, key=lambda x: -x[1][0])
    return next_steps
