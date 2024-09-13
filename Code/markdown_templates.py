header_template = """# Opening Analysis for the board **SPI {index}**: `{board}`

**Overall Statistics:**

| # Matches                | White wins      | Draw           | Black wins      | Average points for White |
|:------------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| {nr_matches}             | {percent_white} | {percent_draw} | {percent_black} | {points}                 |

For all openings, the next moves are sorted by likeliness. We only show those with at least 1/3 of the most likely next move.
"""

openings_template = """## Openings for threshold = {threshold}

| Opening   | Next moves | Likeliness | White wins      | Draw           | Black wins      | Average points for White |
|-----------|------------|:----------:|:---------------:|:--------------:|:---------------:|:------------------------:|
"""

opening_template = """| {opening} | {moves} | {move_prob} | {percent_white} | {percent_draw} | {percent_black} | {points} |"""

board_template = """| {board_index} | [{board_name}](BoardAnalysis/{board_link}.md) | {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} | {points}"""
