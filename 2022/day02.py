from typing import List, Tuple


"""
Part 1 Shapes:
A/X: Rock
B/Y: Paper
C/Z: Scissors

SHAPE_SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
"""

GAME_SCORES = {
    'A': {'X': 4, 'Y': 8, 'Z': 3},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6},
}


def read_file(filename: str) -> List[Tuple]:
    rounds = []
    with open(filename) as f:
        for line in f.readlines():
            round = tuple(line.strip().split(' '))
            rounds.append(round)

    return rounds


def score_round(round: Tuple[str, str],
                scores: dict = GAME_SCORES) -> int:
    return scores[round[0]][round[1]]


def score_rounds(rounds: List[Tuple[str, str]],
                 scores: dict = GAME_SCORES) -> int:
    score = 0

    for round in rounds:
        score = score + score_round(round, scores)

    return score


"""
Part 2 updates
A: Rock (1 pt)
B: Paper (2 pts)
C: Scissors (3 pts)

X: Lose the round (0 pts)
Y: Draw the round (3 pts)
Z: Win the round (6 pts)
"""

GAME_SCORES_2 = {
    'A': {'X': 3+0, 'Y': 1+3, 'Z': 2+6},
    'B': {'X': 1+0, 'Y': 2+3, 'Z': 3+6},
    'C': {'X': 2+0, 'Y': 3+3, 'Z': 1+6},
}


def score_rounds_2(rounds: List[Tuple[str, str]]) -> int:
    return score_rounds(rounds, scores=GAME_SCORES_2)
