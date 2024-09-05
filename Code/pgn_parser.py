import re

def ParseMatch(match):
    meta, match = match.split("\n\n")
    for line in meta.splitlines():
        if line.startswith("[Result"):
            res = line.split('"')
            res = res[1]
            break
    assert res in ["0-1", "1/2-1/2", "1-0"]
    match = " ".join(match.splitlines())
    match = re.sub(r'\{.*?\}', '', match)
    match = re.sub(r'\d+\.\.\.', '', match).strip()
    match = re.sub(r'\s+', ' ', match)
    match = re.sub(r'\d+\.\s*', '', match)
    return match.split(" "), res

test_str = """[Event "Chess960 Game"]
[Site "./"]
[Date "2024.01.15"]
[Round "1"]
[White "Stockfish"]
[Black "Stockfish"]
[Result "0-1"]
[FEN "bqrknnrb/pppppppp/8/8/8/8/PPPPPPPP/BQRKNNRB w KQkq - 0 1"]
[Variant "Chess960"]
[WhiteElo "19"]
[BlackElo "19"]
[TimeControl "3.75+0.0625"]

1. c4 { [%eval 0.17] [%clk 3.751] } 1... g6 { [%eval -0.13] [%clk 0.066] } 2.
g3 { [%eval 0.2] [%clk 0.062] } 2... b6 { [%eval -0.13] [%clk 0.062] } 3. Nf3
{ [%eval 0.25] [%clk 0.062] } 3... c5 { [%eval 0.08] [%clk 0.063] } 4. Ng5
{ [%eval -0.1] [%clk 0.061] } 4... Nd6 { [%eval 0.25] [%clk 0.065] } 5. Bxa8
{ [%eval -0.27] [%clk 0.065] } 5... Qxa8 { [%eval 0.26] [%clk 0.059] } 6. b3
{ [%eval -0.21] [%clk 0.065] } 6... Ne6 { [%eval 0.21] [%clk 0.061] } 7. Nxe6+
{ [%eval -0.19] [%clk 0.062] } 7... dxe6 { [%eval 0.26] [%clk 0.061] } 8. Ne3
{ [%eval -0.27] [%clk 0.064] } 8... Bd4 { [%eval 0.31] [%clk 0.065] } 9. Bxd4
{ [%eval -0.28] [%clk 0.058] } 9... cxd4 { [%eval 0.26] [%clk 0.063] } 10. Nc2
{ [%eval -0.23] [%clk 0.064] } 10... e5 { [%eval 0.35] [%clk 0.06] } 11. d3
{ [%eval -0.19] [%clk 0.063] } 11... Qb7 { [%eval 0.37] [%clk 0.065] } 12. O-O
{ [%eval -0.32] [%clk 0.061] } 12... O-O { [%eval 0.51] [%clk 0.063] } 13. Qb2
{ [%eval -0.38] [%clk 0.06] } 13... Nf5 { [%eval 0.42] [%clk 0.064] } 14. e3
{ [%eval -0.05] [%clk 0.062] } 14... dxe3 { [%eval 0.4] [%clk 0.063] } 15. Qxe5
{ [%eval -0.32] [%clk 0.063] } 15... Rfd8 { [%eval 0.45] [%clk 0.062] } 16.
Rcd1 { [%eval -0.2] [%clk 0.063] } 16... exf2+ { [%eval 0.28] [%clk 0.061] }
17. Rxf2 { [%eval -0.15] [%clk 0.066] } 17... f6 { [%eval 0.17] [%clk 0.062] }
18. Qe6+ { [%eval -0.12] [%clk 0.059] } 18... Kf8 { [%eval 0.13] [%clk 0.064] }
19. Qe1 { [%eval -0.1] [%clk 0.064] } 19... b5 { [%eval 0.55] [%clk 0.063] }
20. Qb4 { [%eval -0.37] [%clk 0.064] } 20... Rd7 { [%eval 0.45] [%clk 0.06] }
21. g4 { [%eval -0.42] [%clk 0.062] } 21... Nh4 { [%eval 0.85] [%clk 0.062] }
22. Qxb5 { [%eval -0.78] [%clk 0.062] } 22... Nf3+ { [%eval 0.3] [%clk 0.063] }
23. Kf1 { [%eval -0.14] [%clk 0.064] } 23... Qxb5 { [%eval 0.05] [%clk 0.063] }
24. cxb5 { [%eval -0.14] [%clk 0.059] } 24... Kf7 { [%eval 0.21] [%clk 0.065] }
25. Ne3 { [%eval 0.0] [%clk 0.061] } 25... Ng5 { [%eval 0.0] [%clk 0.064] } 26.
Nc4 { [%eval 0.48] [%clk 0.061] } 26... Nh3 { [%eval -0.32] [%clk 0.067] }"""
