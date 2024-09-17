# Opening Analysis for Chess960: Project Description

**What is an Opening:**

An opening is an initial sequence of moves made by both players, where each move is considered (nearly) optimal based on established principles and strategies.
At any given stage of the opening, both player have a strong incentive to stay in the given progression as deviating could result in suboptimal positions.

**Objective:**

Identify openings for all Chess960 variants.

**Our Approach:**

- **Formalize Openings:** We formalize the above intuitive definition of an opening, based on a dataset of Chess960 games.
- **Identify Openings:** We identify openings for all Chess960 variants through this formalized approach.

**Our Experiments:**

We applied our method to two key datasets:

1. Classical chess games downloaded from [Lichess](https://database.lichess.org/).
2. Chess960 games we generated using the super-human capabilities of [Stockfish 16](https://stockfishchess.org/).

**Key Discoveries:**

- **Lichess Dataset:**
  - This dataset did not lead to meaningful openings.
- **Stockfish Dataset:**
  - We rediscovered traditional chess openings.
  - We identified novel openings across various Chess960 variants.
  - We discuss why the above intuitive definition of opening and the formal definition given below coincide for this dataset.

**Looking Ahead:**

Our methods may as well be applied to other datasets of chess games, or to entirely different types of games to gain new insights.

---

## Defining a Opening

_We now give the technical definitions of a "board", a "game", and an "opening."_

### Basic Concepts

- **Board:** A board is an initial state and rules how to proceed through a series of valid moves, alternating between the two players.
- **Game:** A game is a sequence of these valid moves, culminating in a result: win (1), loss (0), or draw (1/2), seen from the player doing the first move.

Moreover:
- A game’s current state dictates which possible next moves are valid.
- Each valid move modifies the current state, leading to the next state.
- The game's result is determined by the entire sequence of valid moves from the initial state.

### An Opening

An opening of a board (such as standard chess or a Chess960 variant) depends on:
1. A dataset **D** of many games of the board.
2. A threshold **t** which is a value between 0 and 1.

**Opening of a board:**
This is a longest initial sequence of moves that appears in at least the fraction **t** of the games in the dataset **D**.

Longest means that if you add one more move it appears in less than the fraction **t** of games.

For example the threshold value **t=1/10** means that an opening appears in at least every 10th game.

---

## Discoveries

### Threshold Analysis

Identifying openings within a dataset depends on selecting a **threshold** value between 0 and 1.
This threshold determines how often an initial sequence of moves must occur to be considered an opening.
A higher threshold means that an initial sequence must have been played in the dataset more frequently to be recognized.

#### Threshold Sensitivity:

Consider two thresholds, **t1 < t2**.
By definition, if a sequence of moves qualifies as an opening under the lower threshold **t1**, then (a prefix of) this sequence will also be an opening under the higher threshold **t2**.

This means in particular, that one sees the base of an opening for a larger threshold which then branches out into multiple variations of the same opening when lowering the threshold.
This is a well-known phenomenon in classical chess, see for example the [many variations of the **Ruy Lopez** opening](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).
This phenomenon can be seen in several variations of this opening that we can identify in the analysis of [classical chess](https://github.com/stumpc5/chess960/blob/main/BoardAnalysis/rnbqkbnr.md), such as [Queen's Gambit](https://www.chess.com/openings/Queens-Gambit), [Sicilian Defnese](https://www.chess.com/openings/Sicilian-Defense), and the [Ruy Lopez](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).

**Observation:** The given formal definition of opening recovers multiple important well-known openings for classical chess.

### Lichess Data

We analyzed approximately **100 million games** from the [Lichess database](https://database.lichess.org/). However, this dataset did not provide significant insights into Chess960 openings, nor did it for traditional chess. The primary reasons were:

- **Insufficient high-level games**: There were not enough games played at the highest levels to accurately identify optimal or near-optimal moves.
- **Prevalence of blitz games**: Many games were blitz games, where time constraints prevented players from consistently making optimal moves.

Due to these limitations, we decided not to use the Lichess dataset for Chess960 opening analysis.

**TBA:** clarify

### Stockfish Data

To overcome the limitations of human games, we turned to [Stockfish 16](https://stockfishchess.org/), running it at super-human skill levels.
Stockfish played **20,000 games** for each of the 960 different Chess960 starting positions.

#### Game Setup

Here are the key settings we used for these games:

| **Attribute**                | **Value**            |
|------------------------------|----------------------|
| **Skill Level**              | 18-20                |
| **CPU Threads per Game**     | 4                    |
| **Total Time per Game**      | 3.75 sec             |
| **Max Time per Move**        | 0.0625 sec           |

Both players were always at the same skill level to ensure consistency.

#### Defining Openings: Intuition vs. Formality

Since the games were played at a super-human level, we assumed that a move sequence qualifies as an "opening" if it appears frequently enough across all games.
At each step, both players made optimal (or near-optimal) moves.

#### Key Theoretical Insight:

The super-human level and the large number of analyzed games ensure that the formal and intuitive definitions of an opening coincide within this dataset.
The formal definition can therefore be used to idenfity openings for the various Chess960 openings.
