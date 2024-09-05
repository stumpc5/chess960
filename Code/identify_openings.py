def IdentifyOpenings(matches, threshold):
    """
    Identifies the most common chess openings in a list of matches and calculates the percentages of white wins, draws, and black wins after those openings.

    An opening is included if the percentages of matches starting with this opening is at least the threshold, while adding any additional step drops below the threshold.

    Args:
        matches (List[Tuple[Tuple[str], float]]): A list of tuples where each tuple contains the moves as strings and the game result as a float.
        threshold (float): A value between 0 and 1 representing the minimum percentage of matches that should start with a specific opening.

    Returns:
        Tuple:
            - (int, Tuple[float, float, float]): A tuple containing:
                - The total number of matches.
                - The percentage of white wins, draws, and black wins overall.
            - List[Tuple[List[str], Tuple[float, float, float]]]: A list of tuples where each tuple contains:
                - A list of moves representing the opening.
                - A tuple with the percentage of white wins, draws, and black wins after that opening.
    """
    if not (0 <= threshold <= 1):
        raise ValueError("Threshold must be between 0 and 1")

    openings = []
    to_test = [[]]  # Sequences of moves to test

    # Build possible openings based on the match data
    while to_test:
        current_opening = to_test.pop()
        next_steps = BetterOpenings(matches, [step for step, _ in current_opening])

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
    nr_matches = len(matches)
    if nr_matches == 0:
        raise ValueError("No matches provided")

    white_wins = sum(1 for _, result in matches if result == 1.0) / nr_matches
    draws      = sum(1 for _, result in matches if result == 0.5) / nr_matches
    black_wins = sum(1 for _, result in matches if result == 0.0) / nr_matches

    winning_summary = (nr_matches, (white_wins, draws, black_wins))

    # Sort openings by the length of the move sequence
    sorted_openings = sorted(openings, key=lambda opening: len(opening[0]))

    return winning_summary, sorted_openings

def BetterOpenings(matches, opening):
    """
    Finds potential next moves in matches that extend a given opening sequence and calculates win percentages after those moves.

    Args:
        matches (List[Tuple[Tuple[str], float]]): A list of tuples where each tuple contains the moves as strings and the game result as a float.
        opening (List[str]): A prefix (sequence of moves) to look for in the matches.

    Returns:
        List[Tuple[str, Tuple[float, Tuple[float, float, float]]]]: A list of tuples where each tuple contains:
            - The next move that can extend the opening.
            - A tuple with:
                - The percentage of total matches that continue with this move.
                - A tuple of the percentage of white wins, draws, and black wins after this move.
    """
    next_steps: Dict[str, Tuple[int, Tuple[int, int, int]]] = {}
    opening_length = len(opening)

    for match, result in matches:
        if opening_length < len(match):
            for i in range(opening_length):
                if match[i] != opening[i]:
                    break
            else:
                # Found a match for the opening prefix
                next_move = match[opening_length]
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

    total_matches = len(matches)

    # Calculate the percentages of white wins, draws, and black wins for each next move
    next_steps = [
        (move, (count / total_matches, (white / count, draw / count, black / count)))
        for move, (count, (white, draw, black)) in next_steps.items()
        if count > 0
    ]
    next_steps = sorted(next_steps, key=lambda x: -x[1][0])
    return next_steps
