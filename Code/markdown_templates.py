header_template = """# Opening Analysis for the board `{board}`

**Overall Statistics:**

| # Matches                | White wins      | Draw           | Black wins      |
|:------------------------:|:---------------:|:--------------:|:---------------:|
| {nr_matches}             | {percent_white} | {percent_draw} | {percent_black} |

For all openings, the next moves are sorted by likeliness. We only show those with at least 1/3 of the most likely next move.
"""

openings_template = """## Openings for threshold = {threshold}

| Opening   | Next moves | Likeliness | White wins      | Draw           | Black wins      |
|-----------|------------|:----------:|:---------------:|:--------------:|:---------------:|
"""

opening_template = """| {opening} | {moves} | {move_prob} | {percent_white} | {percent_draw} | {percent_black} |"""

board_template = """| [{board_name}](BoardAnalysis/{board_link}.md) | {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} |"""
