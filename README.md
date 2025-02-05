# Opening Analysis for Chess960

**This project is still under development**

Next major steps:

- [ ] Identify the best setup to re-run all 960 x 20.000 games in SF17.
- [ ] Plot, for the standard opening and maybe one other opening, the white/black wins and draws for up to 50-100k games.

## Objective

Identify optimal openings.

* We analyze about **20 million Chess960 games** generated with **Stockfish 16**.

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
| 518 | [RNBQKBNR](BoardAnalysis/rnbqkbnr.md) | 20000            | 24.4% | 58.1% | 17.4% | 0.535 |
| 534 | [RNBKQBNR](BoardAnalysis/rnbkqbnr.md) | 20000            | 31.7% | 51.4% | 16.9% | 0.574 |

[Results for all 960 starting positions](analysis_overview.md)

## Raw data

The complete 20.000 played games per starting position in ``pgn.tar.gz`` format is available at [https://ruhr-uni-bochum.sciebo.de/s/mlGqHPYH8orXHS0](https://ruhr-uni-bochum.sciebo.de/s/mlGqHPYH8orXHS0).

**Password:** Board name with highest average points for white in all caps.
**Hint:** The board has **SPI 935**.

## Feedback

Please send an email to christian.stump@rub.de and to dorpalen-barry@tamu.edu for any feedback.

* Do you have comments about our Stockfish setup?
  - Do you see better ways to generate datasets?
  - Would it be reasonable to increase the database size?

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

* [Galen Dorpalen-Barry](https://galen.dorpalen-barry.org/) (Texas A&M, USA)
* [Christian Stump](https://homepage.rub.de/christian.stump/) (Ruhr University Bochum, Germany)

## Acknowledgements

* The experiments were conducted using large computers at both involved universities.
* The authors thank **Nathan Chapelier-Laget**, **Torsten Hoge**, and **Alexander Ivanov** for useful discussions.

## License

The work in this repository is licensed under the [CC BY-NC license](https://creativecommons.org/licenses/by-nc/4.0/). The license is found [here](/LICENSE.md).
