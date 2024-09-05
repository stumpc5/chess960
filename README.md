# Project Description

We analyze about **20 million Chess960 matches** generated with **Stockfish 16**, more than **20.000 matches for each starting position**.

**Objective:** Identifying optimal openings.

**Details:** [Project description](project_description.md).

# Results

| Board                            | # Played Matches        | White           | Draw           | Black           |
|----------------------------------|:-----------------------:|:---------------:|:--------------:|:---------------:|
| [BBNNQRKR](BoardAnalysis/bbnnqrkr.md) | 1000            | 44.9% | 27.5% | 27.6% |
| [BBNNRKQR](BoardAnalysis/bbnnrkqr.md) | 1000            | 39.8% | 29.5% | 30.7% |
| [BBNNRKRQ](BoardAnalysis/bbnnrkrq.md) | 1000            | 48.3% | 23.5% | 28.2% |
| [BBNNRQKR](BoardAnalysis/bbnnrqkr.md) | 1000            | 38.4% | 29.2% | 32.4% |
| [BBNQNRKR](BoardAnalysis/bbnqnrkr.md) | 1000            | 38.8% | 30.7% | 30.5% |
| [BBNQRKNR](BoardAnalysis/bbnqrknr.md) | 1000            | 37.9% | 30.9% | 31.2% |
| [BBNQRKRN](BoardAnalysis/bbnqrkrn.md) | 1000            | 39.5% | 29.5% | 31.0% |
| [BBNQRNKR](BoardAnalysis/bbnqrnkr.md) | 1000            | 41.2% | 26.7% | 32.1% |
| [BBNRKNQR](BoardAnalysis/bbnrknqr.md) | 1000            | 38.5% | 30.4% | 31.1% |
| [BBNRKNRQ](BoardAnalysis/bbnrknrq.md) | 1000            | 42.8% | 26.9% | 30.3% |

# Comparison to other Chess960 databases

## The "Chess960 Win by Position Setup" data

An analysis of more than 4 million Chess960 matches from Lichess has been conducted [here](https://github.com/welyab/chess960-win-by-position-setup).

TBA

## No variation is better than another

Using A/B testing, 14 million Chess960 matches from Lichess were analyzed [here](https://towardsdatascience.com/analyzing-chess960-data-da5c8cdb01de).

TBA

# Authors

* Galen Dorpalen-Barry (Texas A&M, USA)
* Christian Stump (Ruhr University Bochum, Germany)

# Acknowledgements

* This README was automatically filled with the data.
* The experiments were conducted using large computers at both involved universities.
* The authors thank Nathan Chapelier-Laget and Alexander Ivanov for useful discussions.

# Licence

The work in this repository is licensed under the [CC BY-NC license](https://creativecommons.org/licenses/by-nc/4.0/). The license is found [here](/LICENSE.md).
