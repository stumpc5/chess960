from read_pgn           import ReadPGN
from starting_positions import AllStartingPositions
from identify_openings  import IdentifyOpenings
from markdown_templates import header_template, openings_template, opening_template

def GenerateOpeningTable(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True):
    matches = ReadPGN(board, verbose=verbose)

    openings_table = dict()
    winning  = 0

    for threshold in thresholds:
        stats, openings = IdentifyOpenings(matches, threshold)
        openings_table[threshold] = openings

    return stats, openings_table

def GenerateMarkdown(board="rnbqkbnr", thresholds=[0.01, 0.02, 0.05], verbose=True):
    stats, opening_tables = GenerateOpeningTable(board=board, thresholds=thresholds, verbose=verbose)

    # formating the header
    nr_matches, (percent_white, percent_draw, percent_black) = stats
    header_data = {
        'board'         : board,
        'nr_matches'    : nr_matches,
        'percent_white' : ToPer(percent_white),
        'percent_draw'  : ToPer(percent_draw),
        'percent_black' : ToPer(percent_black),
    }
    header = header_template.format(**header_data)

    #formating each opening and append it to the opening header
    for threshold in reversed(sorted(opening_tables)):
        openings = opening_tables[threshold]

        #formating the opening heading
        threshold_data = {
            'threshold' : threshold
        }
        openings_header = openings_template.format(**threshold_data)

        for opening, moves in openings:
            print(moves)
            opening_data = {
                'opening'       : " &rarr; ".join(opening),
                'moves'         : " <p> ".join(move for move,_ in moves),
                'percent_white' : " <p> ".join(ToPer(per[0]) for _,(_,per) in moves),
                'percent_draw'  : " <p> ".join(ToPer(per[1]) for _,(_,per) in moves),
                'percent_black' : " <p> ".join(ToPer(per[2]) for _,(_,per) in moves),
            }
            opening_tmp = opening_template.format(**opening_data)
            openings_header += opening_tmp + "\n"
        header += "\n\n" + openings_header

    return header

def ToPer(x):
    return str(round(x*1000)/10) + "%"
