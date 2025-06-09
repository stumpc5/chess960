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

## Results

Here is the example for the standard opening and the opening with Queen and King interchanged, indexed by their [Starting Position Index](https://en.wikipedia.org/wiki/Fischer_random_chess_numbering_scheme).
We rediscover well-known openings and their variations, such as [Queen's Gambit](https://www.chess.com/openings/Queens-Gambit), [Sicilian Defense](https://www.chess.com/openings/Sicilian-Defense), and the [Ruy Lopez](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).
Click on the board link for details.

| SPI | Board                            | # Played Games        | White           | Draw           | Black           | Average points for White |
|:-----:|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| 518 | [RNBQKBNR](BoardAnalysis/2025-06_SF17.1/rnbqkbnr.md) | 50000            | 11.1% | 83.9% | 5.0% | 0.531 |
| 534 | [RNBKQBNR](BoardAnalysis/2025-06_SF17.1/rnbkqbnr.md) | 50000            | 10.0% | 82.9% | 7.1% | 0.515 |

### Results Overview

The [Results Overview Page](BoardAnalysis/2025-06_SF17.1_analysis_overview.md) shows each starting position, either [ordered by starting position](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-starting-position-index) or [ordered by average points for White](BoardAnalysis/2025-06_SF17.1_analysis_overview.md#sorted-by-average-points-for-white).

### Results for Individual Starting Positions

Each starting position has its own page linked from the overview page. It shows

* The average time and number of moves per game, 
* the most common openings and their variants.

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
