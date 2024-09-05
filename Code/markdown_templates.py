header_template = """# Opening Analysis for the board `{board}`

**Overall Statistics:**

| #Matches                | White           | Draw           | Black           |
|:-----------------------:|:---------------:|:--------------:|:---------------:|
| {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} |

"""

openings_template = """## Openings for threshold = {threshold}

(We only show those next moves that happen with at least 1/3 of the likelihood of the most likely next move.)

| Opening   | Next moves | Opening percentage  | White wins      | Draw           | Black wins      |
|-----------|------------|:----------:|:---------------:|:--------------:|:---------------:|
"""

opening_template = """| {opening} | {moves} | {move_prob} | {percent_white} | {percent_draw} | {percent_black} |"""

board_template = """| [{board_name}](BoardAnalysis/{board_link}.md) | {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} |"""
