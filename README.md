# Opening Analysis for Chess960

**Objective:** Identifying optimal openings.

**Details:** We analyze about **20 million Chess960 matches** generated with **Stockfish 16**, more than **20.000 matches for each starting position**. Details are found in the [project description](project_description.md).

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
| [BBNRKQNR](BoardAnalysis/bbnrkqnr.md) | 1000            | 37.4% | 30.7% | 31.9% |
| [BBNRKQRN](BoardAnalysis/bbnrkqrn.md) | 1000            | 43.1% | 27.1% | 29.8% |
| [BBNRKRNQ](BoardAnalysis/bbnrkrnq.md) | 1000            | 48.5% | 24.1% | 27.4% |
| [BBNRKRQN](BoardAnalysis/bbnrkrqn.md) | 1000            | 43.1% | 29.6% | 27.3% |
| [BBNRNKQR](BoardAnalysis/bbnrnkqr.md) | 1000            | 42.7% | 26.9% | 30.4% |
| [BBNRNKRQ](BoardAnalysis/bbnrnkrq.md) | 1000            | 44.3% | 25.9% | 29.8% |
| [BBNRNQKR](BoardAnalysis/bbnrnqkr.md) | 1000            | 41.6% | 30.3% | 28.1% |
| [BBNRQKNR](BoardAnalysis/bbnrqknr.md) | 1000            | 44.3% | 30.8% | 24.9% |
| [BBNRQKRN](BoardAnalysis/bbnrqkrn.md) | 1000            | 38.2% | 32.4% | 29.4% |
| [BBNRQNKR](BoardAnalysis/bbnrqnkr.md) | 1000            | 41.3% | 30.6% | 28.1% |
| [BBQNNRKR](BoardAnalysis/bbqnnrkr.md) | 1000            | 34.6% | 29.7% | 35.7% |
| [BBQNRKNR](BoardAnalysis/bbqnrknr.md) | 1000            | 36.4% | 28.8% | 34.8% |
| [BBQNRKRN](BoardAnalysis/bbqnrkrn.md) | 1000            | 40.5% | 28.5% | 31.0% |
| [BBQNRNKR](BoardAnalysis/bbqnrnkr.md) | 1000            | 42.4% | 27.0% | 30.6% |
| [BBQRKNNR](BoardAnalysis/bbqrknnr.md) | 1000            | 39.2% | 31.1% | 29.7% |
| [BBQRKNRN](BoardAnalysis/bbqrknrn.md) | 1000            | 39.4% | 29.3% | 31.3% |
| [BBQRKRNN](BoardAnalysis/bbqrkrnn.md) | 1000            | 45.8% | 28.0% | 26.2% |
| [BBQRNKNR](BoardAnalysis/bbqrnknr.md) | 1000            | 40.8% | 30.1% | 29.1% |
| [BBQRNKRN](BoardAnalysis/bbqrnkrn.md) | 1000            | 32.7% | 38.2% | 29.1% |
| [BBQRNNKR](BoardAnalysis/bbqrnnkr.md) | 1000            | 36.9% | 32.3% | 30.8% |
| [BBRKNNQR](BoardAnalysis/bbrknnqr.md) | 1000            | 40.4% | 32.1% | 27.5% |
| [BBRKNNRQ](BoardAnalysis/bbrknnrq.md) | 1000            | 46.7% | 27.3% | 26.0% |
| [BBRKNQNR](BoardAnalysis/bbrknqnr.md) | 1000            | 38.1% | 30.1% | 31.8% |
| [BBRKNQRN](BoardAnalysis/bbrknqrn.md) | 1000            | 40.8% | 34.0% | 25.2% |
| [BBRKNRNQ](BoardAnalysis/bbrknrnq.md) | 1000            | 41.6% | 29.5% | 28.9% |
| [BBRKNRQN](BoardAnalysis/bbrknrqn.md) | 1000            | 37.5% | 29.1% | 33.4% |

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
