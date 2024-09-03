# Identifying Chess960 Openings

**Objective:**

Discover possible openings for Chess960 variants.

**Who Should Read This:**

- Amateur and professional Chess960 players.
- Anyone curious about the scientific analysis of Chess960 openings.

**Our Approach:**

- **Game and Match Definitions:** We explain what constitutes a "game" and a "match".
- **Opening Identification:** We define an "opening" based on a dataset of matches and a specific threshold.

**Our Experiments:**

We applied our method to two key datasets:

1. Classical chess matches downloaded from [Lichess](https://database.lichess.org/).
2. Chess960 matches we generated using the super-human capabilities of [Stockfish](https://stockfishchess.org/).

**Key Discoveries:**

- **Lichess Dataset:** This dataset did not lead to meaningful openings.
- **Stockfish Dataset:** We obtained several interesting results:
  - The threshold value stabilized, suggesting a universal threshold for defining openings.
  - With this threshold, we:
    - Rediscovered traditional chess openings.
    - Identified novel openings across various Chess960 variants.

**Looking Ahead:**

Our methods may as well be applied to other datasets of chess matches, or to entirely different games to explore new insights.

---

## The Game of Chess

_Before diving into technical details, we revisit how chess matches are recorded._

The starting position in classical chess is
`rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`
(in [FEN notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)).

A typical initial move might be `e4 e5`, changing the board state to
`rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1`.

Matches are recorded in [PGN notation](https://en.wikipedia.org/wiki/Portable_Game_Notation) like this:

    1. e4 e5 2. Nf3 Nc6 3. Bb5 3... a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5 Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6 23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5 35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6 Nf2 42. g4 Bd3 43. Re6 1/2-1/2

This sequence of moves ends in a draw, marked as `1/2-1/2`.

### Chess960

In [Chess960](https://en.wikipedia.org/wiki/Fischer_random_chess), also known as Fischer Random Chess:
- Pieces on the home ranks are **randomly arranged**, mirroring both players.
- The setup follows two rules:
  1. Bishops are placed on opposite-colored squares.
  2. The king is positioned between the two rooks.

There are **960 possible starting positions** that meet these criteria, giving the variant its name.

---

## Defining a Game

_We now delve into the technical definitions of a "game" and a "match."_

### Basic Concepts

- **Game:** A game starts with an initial state and proceeds through a series of valid moves.
- **Match:** A match is a sequence of these valid moves, culminating in a result: win (1), loss (0), or draw (1/2).

Moreover:
- A game’s current state dictates which moves are valid.
- Each valid move modifies the current state, leading to the next state.
- The match result is determined by the entire sequence of valid moves from the initial state.

## Defining an Opening

An opening in a game (e.g., standard chess or a Chess960 variant) depends on:
1. A dataset **D** of many matches of the game.
2. A threshold **t** which is a percentage between 1 and 100.

**Opening of a game:**
This is the longest sequence of moves that appears in at least **t%** of the matches in the dataset **D**. Longest means that if you add one more move it appears in less than **t%** of matches.

### Examples of Openings

Consider two trivial scenarios:

#### Every Match as an Opening

If the dataset **D** has only 100 matches and the threshold **t** is set to the minimum value of **1%**, then every full match would qualify as an opening.

#### The Empty Opening

If the dataset contains matches with different initial moves and **t** is set to **100%**, the only opening sequence would be... no moves at all.

### Datasets Used

We applied this definition of openings to two datasets:
- Real game data from Lichess.
- Stockfish-generated super-human matches for each Chess960 variant.

### Analysis and Discussion

#### Lichess Data

The Lichess dataset did not yield meaningful insights into openings, not even for standard chess. Reasons include:
- Insufficiently many high-level matches to reflect optimal moves.
- Many matches are blitz games, where players do not have time to make optimal moves.

As a result, we didn’t use this dataset for analyzing Chess960 openings.

#### Stockfish Data

tba
