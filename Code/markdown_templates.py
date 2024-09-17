header_template = """# Opening Analysis **SPI {index}**: `{board}`

**Overall Statistics:**

| # Played Games           | White           | Draw           | Black           | Average points for White |
|:------------------------:|:---------------:|:--------------:|:---------------:|:------------------------:|
| {nr_games}               | {percent_white} | {percent_draw} | {percent_black} | {points}                 |

The openings and the next moves are sorted by likeliness. We show at most the five most likely next moves.
"""

openings_template = """## Openings for threshold = {threshold}

| Opening   | Likeliness | Next moves | Likeliness | White wins      | Draw           | Black wins      | Average points for White |
|-----------|------------|------------|:----------:|:---------------:|:--------------:|:---------------:|:------------------------:|
"""

opening_template = """| {opening} | {opening_prob} | {moves} | {move_prob} | {percent_white} | {percent_draw} | {percent_black} | {points} |"""

board_template = """| {board_index} | [{board_name}](BoardAnalysis/{board_link}.md) | {nr_games}            | {percent_white} | {percent_draw} | {percent_black} | {points}"""
