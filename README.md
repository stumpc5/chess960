# Opening Analysis for Chess960

**This project is still under development**

## Objective

Identify optimal openings.

* We analyze about **20 million Chess960 matches** generated with **Stockfish 16**.

* We give a formal definition of an opening and apply it to the dataset.

* We rediscover well-known chess openings and identify novel openings for all Chess960 variants.

Consult the [project description](project_description.md) for details.

## Who Should Read This

- Amateur and professional Chess960 players.
- Anyone curious about the scientific analysis of Chess960 openings.

## Results

Here is the example for the standard opening and the opening with Queen and King interchanged.
We rediscover well-known openings and their variations, such as the [**Ruy Lopez**](https://www.chess.com/forum/view/chess-openings/all-ruy-lopez-variations).

| Board                            | # Played Matches        | White           | Draw           | Black           |
|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|
| [RNBQKBNR](BoardAnalysis/rnbqkbnr.md) | 19640 | 24.6% | 57.9% | 17.5% |
| [RNBKQBNR](BoardAnalysis/rnbkqbnr.md) | 19640 | 32.0% | 51.1% | 16.9% |

[Results for all 960 starting positions](README_ANALYSIS.md)

## Feedback

Please send an email to christian.stump@rub.de and to dorpalen-barry@tamu.edu for any feedback.

We are in particular interested feedback concerning the following points:

* Do you have comments about our Stockfish setup?
  - Do you see better ways to generate datasets?
  - Would it be reasonable to increase the database size?

* Are there reasonable ways to group openings into categories?
  - The board setup might suggest certain types of opening strategies.
  - Which properties of the board configuration imply which types of openings?

## Comparison to other Chess960 databases

### The "Chess960 Win by Position Setup" data

An analysis of more than 4 million Chess960 matches from Lichess has been conducted [here](https://github.com/welyab/chess960-win-by-position-setup).
We represent [their data in our format](chess960_win_by_position_data.md)  for comparison.

### No variation is better than another

Using A/B testing, 14 million Chess960 matches from Lichess were analyzed [here](https://towardsdatascience.com/analyzing-chess960-data-da5c8cdb01de).

TBA

## Authors

* [Galen Dorpalen-Barry](https://galen.dorpalen-barry.org/) (Texas A&M, USA)
* [Christian Stump](https://homepage.rub.de/christian.stump/) (Ruhr University Bochum, Germany)

## Acknowledgements

* The experiments were conducted using large computers at both involved universities.
* The authors thank Nathan Chapelier-Laget and Alexander Ivanov for useful discussions.

## License

The work in this repository is licensed under the [CC BY-NC license](https://creativecommons.org/licenses/by-nc/4.0/). The license is found [here](/LICENSE.md).
