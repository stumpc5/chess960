# Opening Analysis for Chess960 aka Fischer Random

## Goals

* We analyzed about **100 million games** for all 960 starting positions, generated with **Stockfish 16** and with **Stockfish 17.1**.

* We give a [formal definition of an opening](project_description.md) and apply it to the dataset.

* We identify the best openings for all 960 starting positions.

* We rediscover well-known chess openings and identify novel openings for all Chess960 variants.

## Who Should Read This

- Amateur and professional Chess960 players.
- Anyone curious about the scientific analysis of Chess960 openings.

## Data Setup

We generated 100 million games with Stockfish 16 and Stockfish 17.1 using the following setup:

| **Attribute**                 | **Value**            |
|-------------------------------|----------------------|
| **Skill Level**               | 20                   |
| **CPU Threads per Game**      | 4                    |
| **Time per Game**             | 4.0  sec             |
| **Additional Time per Move**  | 0.05 sec             |

## Results

### Results Overview SF16

*  [Results Overview](BoardAnalysis/2025-06_SF16_analysis_overview.md) / [Sorted by starting position](BoardAnalysis/2025-06_SF16_analysis_overview.md#sorted-by-starting-position-index) / [Sorted by average points for White](BoardAnalysis/2025-06_SF16_analysis_overview.md#sorted-by-average-points-for-white).

### Results Overview SF17.1

* [Results Overview](BoardAnalysis/2025-06_SF17.1_analysis_overview.md) / [Sorted by starting position](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-starting-position-index) / [Sorted by average points for White](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-average-points-for-white).

### How To Read The Results

The standard opening and the opening with Queen and King interchanged, indexed by their [Starting Position Index](https://en.wikipedia.org/wiki/Fischer_random_chess_numbering_scheme):

| SF | SPI | Board                            | # Played Games        | White           | Draw           | Black           | Average points for White |
|:-----:|:-----:|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| SF16   | 518 | [RNBQKBNR](BoardAnalysis/2025-06_SF16/rnbqkbnr.md) | 50000            | 13.0% | 78.1% |  9.0% | 0.520 |
| SF16   | 534 | [RNBKQBNR](BoardAnalysis/2025-06_SF16/rnbkqbnr.md) | 50000            | 11.1% | 78.7% | 10.2% | 0.504 |
| SF17.1 | 518 | [RNBQKBNR](BoardAnalysis/2025-06_SF17.1/rnbqkbnr.md) | 50000            | 11.1% | 83.9% |  5.0% | 0.531 |
| SF17.1 | 534 | [RNBKQBNR](BoardAnalysis/2025-06_SF17.1/rnbkqbnr.md) | 50000            | 10.0% | 82.9% |  7.1% | 0.515 |

We rediscover well-known openings and their variations, such as [Queen's Gambit](https://www.chess.com/openings/Queens-Gambit), [Sicilian Defense](https://www.chess.com/openings/Sicilian-Defense), and the [Ruy Lopez](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).

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
The Average points for white have not changed significantly, in alignment with the theoretical assumptions on what constitues an opening.

### Fair And Unfair Starting Positions

The following table shows
* the starting position **SPI18** most in favor of White,
* the two starting positions **SPI39** and **SPI671** that are most fair, and
* the starting position **240** most in favor of Black.

| SF | SPI | Board                            | # Played Games        | White           | Draw           | Black           | Average points for White |
|:-----:|:-----:|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| SF17.1   | 18  | [BNQNRBKR](BoardAnalysis/2025-06_SF17.1/bnqnrbkr.md) | 50000            | 44.8% | 51.3% |  3.9% | 0.704 |
| SF17.1   | 39  | [NNBQRKRB](BoardAnalysis/2025-06_SF17.1/nnbqrkrb.md) | 50000            |  9.5% | 81.0% |  9.6% | 0.500 |
| SF17.1   | 671 | [RNKRNQBB](BoardAnalysis/2025-06_SF17.1/rnkrnqbb.md) | 50000            | 11.1% | 77.9% | 11.0% | 0.500 |
| SF17.1   | 240 | [BBNRKQNR](BoardAnalysis/2025-06_SF17.1/bbnrkqnr.md) | 50000            |  9.8% | 77.7% | 12.5% | 0.487 |

(Observe that the differences between White and Black winning in the two most fair starting positions are marginal rounding differences only.)

## Raw data

The following is one randomly chosen game from the dataset:
```
[Event "Opening Analysis, AG Prof. Stump, RUB, Germany"]
[Site "https://github.com/stumpc5/chess960"]
[Date "2025/05/23"]
[Round "1"]
[White "Stockfish 17.1"]
[Black "Stockfish 17.1"]
[Result "1/2-1/2"]
[Variant "Chess960"]
[WhiteSkillLevel "20"]
[BlackSkillLevel "20"]
[TimeControl "4.0+0.05"]
[FEN "bbrnkqrn/pppppppp/8/8/8/8/PPPPPPPP/BBRNKQRN w KQkq - 0 1"]
[NrMoves "23"]
[WallTime "9.739 sec"]

1. c4 { [%clk 3.799] [%eval 0.39] [%depth 19] [%nodes 345565] }
1... c5 { [%clk 3.773] [%eval -0.4] [%depth 17] [%nodes 331111] }
2. f4 { [%clk 3.594] [%eval 0.38] [%depth 15] [%nodes 259374] }
2... g5 { [%clk 3.656] [%eval -0.34] [%depth 14] [%nodes 219920] }
3. b3 { [%clk 3.198] [%eval 0.21] [%depth 16] [%nodes 615956] }
3... gxf4 { [%clk 3.648] [%eval -0.02] [%depth 11] [%nodes 83109] }
4. Bxh7 { [%clk 3.196] [%eval 0.43] [%depth 13] [%nodes 113432] }
4... Rg5 { [%clk 3.551] [%eval -0.01] [%depth 13] [%nodes 187012] }
5. g4 { [%clk 2.84] [%eval 0.37] [%depth 15] [%nodes 444957] }
5... Ng6 { [%clk 3.525] [%eval 0.16] [%depth 13] [%nodes 132538] }
6. Nhf2 { [%clk 2.834] [%eval 0.43] [%depth 13] [%nodes 110197] }
6... Ne6 { [%clk 3.449] [%eval 0.47] [%depth 12] [%nodes 154593] }
7. Ne4 { [%clk 2.449] [%eval -0.53] [%depth 14] [%nodes 478469] }
7... Qh6 { [%clk 3.413] [%eval 0.72] [%depth 15] [%nodes 150052] }
8. Nxg5 { [%clk 2.446] [%eval -0.56] [%depth 11] [%nodes 96351] }
8... Nxg5 { [%clk 3.37] [%eval 0.66] [%depth 12] [%nodes 80104] }
9. Bxg6 { [%clk 2.395] [%eval -0.53] [%depth 11] [%nodes 127731] }
9... fxg6 { [%clk 3.227] [%eval 0.7] [%depth 13] [%nodes 229570] }
10. Nc3 { [%clk 1.956] [%eval -0.36] [%depth 14] [%nodes 404119] }
10... Nh3 { [%clk 2.634] [%eval 0.5] [%depth 15] [%nodes 631322] }
11. Rg2 { [%clk 1.927] [%eval -0.21] [%depth 11] [%nodes 104460] }
11... b6 { [%clk 2.594] [%eval 0.51] [%depth 11] [%nodes 114815] }
12. Kd1 { [%clk 1.91] [%eval -0.26] [%depth 12] [%nodes 109778] }
12... Be5 { [%clk 2.054] [%eval 0.11] [%depth 15] [%nodes 595203] }
13. Nb5 { [%clk 1.831] [%eval -0.27] [%depth 12] [%nodes 131114] }
13... Bb8 { [%clk 1.908] [%eval 0.03] [%depth 13] [%nodes 191892] }
14. Nc3 { [%clk 1.818] [%eval -0.18] [%depth 12] [%nodes 83012] }
14... e6 { [%clk 1.837] [%eval 0.06] [%depth 16] [%nodes 124745] }
15. d3 { [%clk 1.751] [%eval 0.06] [%depth 12] [%nodes 128343] }
15... Ng5 { [%clk 1.751] [%eval 0.0] [%depth 13] [%nodes 149524] }
16. Rf2 { [%clk 1.677] [%eval 0.0] [%depth 24] [%nodes 144549] }
16... Nh3 { [%clk 1.756] [%eval 0.0] [%depth 18] [%nodes 74812] }
17. Rg2 { [%clk 1.617] [%eval 0.0] [%depth 37] [%nodes 151451] }
17... Ng5 { [%clk 1.732] [%eval 0.0] [%depth 20] [%nodes 88976] }
18. Rf2 { [%clk 1.588] [%eval 0.0] [%depth 22] [%nodes 78212] }
18... Nh3 { [%clk 1.692] [%eval 0.0] [%depth 26] [%nodes 138011] }
19. Rg2 { [%clk 1.447] [%eval 0.0] [%depth 24] [%nodes 172620] }
19... Ng5 { [%clk 1.689] [%eval 0.0] [%depth 27] [%nodes 71174] }
20. Rf2 { [%clk 1.467] [%eval 0.0] [%depth 17] [%nodes 52138] }
20... Nh3 { [%clk 1.669] [%eval 0.0] [%depth 32] [%nodes 86421] }
21. Rg2 { [%clk 1.47] [%eval 0.0] [%depth 27] [%nodes 138073] }
21... Ng5 { [%clk 1.629] [%eval 0.0] [%depth 29] [%nodes 96286] }
22. Rf2 { [%clk 1.437] [%eval 0.0] [%depth 27] [%nodes 97500] }
22... Nh3 { [%clk 1.634] [%eval 0.0] [%depth 35] [%nodes 88062] }
23. Rg2 { [%clk 1.388] [%eval 0.0] [%depth 28] [%nodes 119623] } 1/2-1/2
```

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
