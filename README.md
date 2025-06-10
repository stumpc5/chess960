# Opening Analysis for Chess960

Next steps:

- [ ] Plot, for the standard opening and maybe one other opening, the white/black wins and draws for up to 50-100k games.

## Objective

Identify optimal openings.

* We analyzed about **100 million Chess960 games** generated with **Stockfish 16** and with **Stockfish 17.1**.

* We give a formal definition of an opening and apply it to the dataset.

* We rediscover well-known chess openings and identify novel openings for all Chess960 variants.

Consult the [project description](project_description.md) for details.

## Who Should Read This

- Amateur and professional Chess960 players.
- Anyone curious about the scientific analysis of Chess960 openings.

## Data Setup

We generated 100 million games with Stockfish 16 and Stockfish 17.1 using the following setup:

| **Attribute**                | **Value**            |
|------------------------------|----------------------|
| **Skill Level**              | 20                   |
| **CPU Threads per Game**     | 4                    |
| **Total Time per Game**      | 4.0  sec             |
| **Max Time per Move**        | 0.05 sec             |

TBA: Add why we chose exactly this setup.

## Results

### Results Overview SF16

*  [Results Overview](BoardAnalysis/2025-06_SF16_analysis_overview.md) / [Sorted by starting position](BoardAnalysis/2025-06_SF16_analysis_overview.md#sorted-by-starting-position-index) / [Sorted by average points for White](BoardAnalysis/2025-06_SF16_analysis_overview.md#sorted-by-average-points-for-white).

### Results Overview SF17.1

* [Results Overview](BoardAnalysis/2025-06_SF17.1_analysis_overview.md) / [Sorted by starting position](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-starting-position-index) / [Sorted by average points for White](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-average-points-for-white).

### How To Read The Results

Here is the example for the standard opening and the opening with Queen and King interchanged, indexed by their [Starting Position Index](https://en.wikipedia.org/wiki/Fischer_random_chess_numbering_scheme).
We rediscover well-known openings and their variations, such as [Queen's Gambit](https://www.chess.com/openings/Queens-Gambit), [Sicilian Defense](https://www.chess.com/openings/Sicilian-Defense), and the [Ruy Lopez](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).
Click on the board link for details.

| SF | SPI | Board                            | # Played Games        | White           | Draw           | Black           | Average points for White |
|:-----:|:-----:|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| SF16   | 518 | [RNBQKBNR](BoardAnalysis/2025-06_SF16/rnbqkbnr.md) | 50000            | 13.0% | 78.1% |  9.0% | 0.520 |
| SF16   | 534 | [RNBKQBNR](BoardAnalysis/2025-06_SF16/rnbkqbnr.md) | 50000            | 11.1% | 78.7% | 10.2% | 0.504 |
| SF17.1 | 518 | [RNBQKBNR](BoardAnalysis/2025-06_SF17.1/rnbqkbnr.md) | 50000            | 11.1% | 83.9% |  5.0% | 0.531 |
| SF17.1 | 534 | [RNBKQBNR](BoardAnalysis/2025-06_SF17.1/rnbkqbnr.md) | 50000            | 10.0% | 82.9% |  7.1% | 0.515 |

Each starting position has its own page showing

* the average time and number of moves per game, and
* the most common openings and their variants.

For **classical chess with SF17.1**, we identify the following most common opening among the 50.000 games:

| Opening   | Likeliness | Next moves | Likeliness | White wins      | Draw           | Black wins      | Average points for White |
|-----------|------------|------------|:----------:|:---------------:|:--------------:|:---------------:|:------------------------:|
|  1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.Re1 Nd6 6.Nxe5 Be7 7.Bf1 Nxe5 8.Rxe5 O-O 9.d4 | 13.6% | Ne8 <p> Bf6 | 7.2% <p> 6.4% | 6.7% <p> 5.4% | 89.7% <p> 91.4% | 3.6% <p> 3.2% | 0.516 <p> 0.511 |

This is an [open variation of the Berlin Defence of the Ruy Lopez](https://chessopenings.com/eco/C67/).
Is has been played in 13.6% of the games and the next most common move is 9...Ne8, which has been played in 7.2% of the games.

Overall, White wins 13.0% of the games, while it only wins 6.7% of the games in this variant.

### Fair And Unfair Starting Positions

The following table shows
* the starting position most in favor of White,
* the two starting positions that are most fair, and
* the starting position most in favor of Black.

| SF | SPI | Board                            | # Played Games        | White           | Draw           | Black           | Average points for White |
|:-----:|:-----:|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| SF17.1   | 18  | [BNQNRBKR](BoardAnalysis/2025-06_SF17.1/bnqnrbkr.md) | 50000            | 44.8% | 51.3% |  3.9% | 0.704 |
| SF17.1   | 39  | [NNBQRKRB](BoardAnalysis/2025-06_SF17.1/nnbqrkrb.md) | 50000            |  9.5% | 81.0% |  9.6% | 0.500 |
| SF17.1   | 671 | [RNKRNQBB](BoardAnalysis/2025-06_SF17.1/rnkrnqbb.md) | 50000            | 11.1% | 77.9% | 11.0% | 0.500 |
| SF17.1   | 240 | [BBNRKQNR](BoardAnalysis/2025-06_SF17.1/bbnrkqnr.md) | 50000            |  9.8% | 77.7% | 12.5% | 0.487 |

(Observe that the differences between W/B in the fair starting positions are marginal rounding differences only.)

## Raw data

The complete 100.000 played games per starting position in ``pgn.tar.gz`` format is available at [https://ruhr-uni-bochum.sciebo.de/s/mlGqHPYH8orXHS0](https://ruhr-uni-bochum.sciebo.de/s/mlGqHPYH8orXHS0).

To request access to the raw data, please send an email to [Christian Stump](mailto:christian.stump@rub.de).

## Feedback

For any feedback, please send an email to [Christian Stump](mailto:christian.stump@rub.de).

* Do you have comments about our Stockfish setup?
  - Do you see better ways to generate datasets?

* Are there reasonable ways to group openings into categories?
  - The board setup might suggest certain types of opening strategies.
  - Which properties of the board configuration imply which types of openings?

## Comparison to other Chess960 databases

The following two projects have both analyzed Chess960 games from Lichess.

### The "Chess960 Win by Position Setup" data

An analysis of more than 4 million Chess960 games from Lichess has been conducted [here](https://github.com/welyab/chess960-win-by-position-setup).
We represent [their data in our format](chess960_win_by_position_data.md)  for comparison.

They conclude that "white pieces have an advantage, \[and that\] the positions setup where black have an advantage are expressively less that positions where white won more."

### No variation is better than another

Using A/B testing, 14 million Chess960 games from Lichess were analyzed [here](https://towardsdatascience.com/analyzing-chess960-data-da5c8cdb01de).

They conclude that "there are no starting positions that favor any of the players more than other positions."

## Authors

This project was initiated and is maintained by [Christian Stump](https://homepage.rub.de/christian.stump/) (Ruhr University Bochum, Germany).
The first version was created in collaboration with [Galen Dorpalen-Barry](https://galen.dorpalen-barry.org/) (Texas A&M, USA) and the second version in collaboration with [Nupur Jain](https://math.ruhr-uni-bochum.de/fakultaet/arbeitsbereiche/algebra/research-team-stump/team/nupur-jain/) (Ruhr University Bochum, Germany).

## Acknowledgements

* The authors thank **Ingo Althöfer**, **Nathan Chapelier-Laget**, **Torsten Hoge**, and **Alexander Ivanov** for useful discussions.

## License

The work in this repository is licensed under the [CC BY-NC license](https://creativecommons.org/licenses/by-nc/4.0/). The license is found [here](/LICENSE.md).
