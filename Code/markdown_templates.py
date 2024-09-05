header_template = """# Opening Analysis for the board `{board}`

**Overall Statistics:**

| #Matches                | White           | Draw           | Black           |
|:-----------------------:|:---------------:|:--------------:|:---------------:|
| {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} |

"""

openings_template = """## Openings for threshold = {threshold}

| Opening   | Next moves | White wins      | Draw           | Black wins      |
|-----------|------------|:---------------:|:--------------:|:---------------:|
"""

opening_template = """| {opening} | {moves}    | {percent_white} | {percent_draw} | {percent_black} |"""

board_template = """| [{board_name}](BoardAnalysis/{board_link}.md) | {nr_matches}            | {percent_white} | {percent_draw} | {percent_black} |"""
