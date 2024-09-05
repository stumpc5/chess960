# Opening Analysis for Chess960: Project Description

**What is an Opening:**

An opening is an initial sequence of moves made by both players, where each move is considered optimal based on established principles and strategies.
At any given stage of the opening, neither player has an incentive to deviate from the standard progression, as doing so could result in a suboptimal position.

**Objective:**

Discover possible openings for all Chess960 variants.

**Who Should Read This:**

- Amateur and professional Chess960 players.
- Anyone curious about the scientific analysis of Chess960 openings.

**Our Approach:**

- **Formalize Openings:** We formalize the above intuitive definition of an opening, based on a dataset of Chess960 matches.
- **Identify Openings:** We identify openings for all Chess960 variants through this formalized approach.

**Our Experiments:**

We applied our method to two key datasets:

1. Classical chess matches downloaded from [Lichess](https://database.lichess.org/).
2. Chess960 matches we generated using the super-human capabilities of [Stockfish](https://stockfishchess.org/).

**Key Discoveries:**

- **Lichess Dataset:**
  - This dataset did not lead to meaningful openings.
- **Stockfish Dataset:**
  - We rediscovered traditional chess openings.
  - We identified novel openings across various Chess960 variants.
  - We discuss why the above intuitive definition of opening and the formal definition given below coincide for this dataset.

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

Matches may be recorded in [algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)) like this:

    1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Nb8 10. d4 Nbd7 11. c4 c6 12. cxb5 axb5 13. Nc3 Bb7 14. Bg5 b4 15. Nb1 h6 16. Bh4 c5 17. dxe5 Nxe4 18. Bxe7 Qxe7 19. exd6 Qf6 20. Nbd2 Nxd6 21. Nc4 Nxc4 22. Bxc4 Nb6 23. Ne5 Rae8 24. Bxf7+ Rxf7 25. Nxf7 Rxe1+ 26. Qxe1 Kxf7 27. Qe3 Qg5 28. Qxg5 hxg5 29. b3 Ke6 30. a3 Kd6 31. axb4 cxb4 32. Ra5 Nd5 33. f3 Bc8 34. Kf2 Bf5 35. Ra7 g6 36. Ra6+ Kc5 37. Ke1 Nf4 38. g3 Nxh3 39. Kd2 Kb5 40. Rd6 Kc5 41. Ra6 Nf2 42. g4 Bd3 43. Re6 1/2-1/2

This sequence of moves ends in a draw, marked as `1/2-1/2`.

### Chess960

In [Chess960](https://en.wikipedia.org/wiki/Fischer_random_chess), also known as Fischer Random Chess:
- Pieces on the home ranks are **randomly arranged**, mirroring both players.
- The setup follows two rules:
  1. Bishops are placed on opposite-colored squares.
  2. The king is positioned between the two rooks.

There are **960 possible starting positions** that meet these criteria, giving the variant its name.

---

## Defining a Opening

_We now give the technical definitions of a "game", a "match", and an "opening"_

### Basic Concepts

- **Game:** A game starts with an initial state and proceeds through a series of valid moves, alternating between two players.
- **Match:** A match is a sequence of these valid moves, culminating in a result: win (1), loss (0), or draw (1/2), seen from the player doing the first move.

Moreover:
- A game’s current state dictates which possible next moves are valid.
- Each valid move modifies the current state, leading to the next state.
- The match result is determined by the entire sequence of valid moves from the initial state.

### An Opening

An opening in a game (such as standard chess or a Chess960 variant) depends on:
1. A dataset **D** of many matches of the game.
2. A threshold **t** which is a value between 0 and 1.

**Opening of a game:**
This is a longest initial sequence of moves that appears in at least the fraction **t** of the matches in the dataset **D**.

Longest means that if you add one more move it appears in less than the fraction **t** of matches.

#### Examples of Openings

For example the threshold value **t=1/10** means that an opening appears in at least every 10th match.
Consider two trivial scenarios:

##### Every Match as an Opening

If the dataset **D** has only 100 matches and the threshold **t** is set to **t=1/100**, then **every full match** qualifies as an opening.

##### The Empty Opening

If the dataset contains matches with different initial moves and **t** is set to **t=1**, the only opening sequence would be **no moves at all**.

Here’s an improved version of your markdown, making it more engaging and accessible to both amateur and professional Chess960 players, as well as those interested in the scientific analysis of Chess960 openings:

---

## Discoveries

### Threshold Analysis

Identifying openings within a dataset depends on selecting a **threshold** value between 0 and 1.
This threshold determines how often an initial sequence of moves must occur to be considered an opening.
A higher threshold means that an initial sequence must be played more frequently to be recognized.

#### Threshold Sensitivity:
Consider two thresholds, **t1 < t2**. By definition, if a sequence of moves qualifies as an opening under the higher threshold **t2**, then the same sequence (or a prefix thereof) will also be an opening under the lower threshold **t1**.

### Lichess Data

We analyzed approximately **100 million games** from the [Lichess database](https://database.lichess.org/). However, this dataset did not provide significant insights into Chess960 openings, nor did it for traditional chess. The primary reasons were:

- **Insufficient high-level matches**: There were not enough matches played at the highest levels to accurately identify optimal or near-optimal moves.
- **Prevalence of blitz matches**: Many matches were blitz matches, where time constraints prevented players from consistently making optimal moves.

Due to these limitations, we decided not to use the Lichess dataset for Chess960 opening analysis.

**TBA:** clarify

### Stockfish Data

To overcome the limitations of human games, we turned to [Stockfish](https://stockfishchess.org/) (version 16), running it at super-human skill levels.
Stockfish played **20,000 games** for each of the 960 different Chess960 starting positions.

#### Match Setup

Here are the key settings we used for these matches:

| **Attribute**               | **Value**             |
|-----------------------------|-----------------------|
| **Skill Level**              | 18-20                |
| **CPU Threads per Match**    | 4                    |
| **Total Time per Match**     | 3.75 sec             |
| **Max Time per Move**        | 0.0625 sec           |

Both players were always at the same skill level to ensure consistency.

#### Defining Openings: Intuition vs. Formality

Since the matches were played at a super-human level, we assumed that a move sequence qualifies as an "opening" if it appears frequently enough across all games.
At each step, both players made optimal (or near-optimal) moves.

#### Key Theoretical Insight:
The high level of play by Stockfish and the large volume of matches ensure that the formal and intuitive definitions of an opening coincide within this dataset.

#### Visualizing the Results

**TBA**

### Code

**TBA**
