import pytest

from aoc_utils import parse_input_file
from day02 import is_game_possible, fewest_cubes_possible
from math import prod

def game_parser(line: str) -> dict:
    """Parse input string and output a dict
    sample string:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""

    game_str, rounds_str = line.split(":")
    game_results = []

    for round in rounds_str.split(";"):
        cube_counts = {"red": 0, "green": 0, "blue": 0}
        for cube_count in round.split(","):
            count, color = cube_count.strip().split(" ")
            cube_counts[color] = int(count)
        game_results.append(cube_counts)
    
    parsed_game = {
        "game_id": int(game_str.split(" ")[1]),
        "game_results": game_results
    }

    return parsed_game


@pytest.fixture
def ex1_input():
    ex1_input = parse_input_file(filename="day02ex.txt",
                                 parse_line=game_parser)

    return ex1_input


@pytest.fixture
def problem_input():
    problem_input = parse_input_file(filename="day02.txt",
                                 parse_line=game_parser)

    return problem_input


def test_game_parser(ex1_input):
    game_1 = ex1_input[0]
    result1 = game_1["game_results"][0]

    print(ex1_input)

    assert len(ex1_input) == 5
    assert game_1["game_id"] == 1
    assert len(game_1["game_results"]) == 3
    assert result1["blue"] == 3
    assert result1["red"] == 4
    assert result1["green"] == 0


def test_problem_input(problem_input):
    assert len(problem_input) == 100
    assert problem_input[-1]["game_id"] == 100


def test_if_game_possible(ex1_input):
    constraint = (12, 13, 14)
    result = [(g["game_id"], is_game_possible(g, constraint)) for g in ex1_input]
    possible_ids = [r[0] for r in result if r[1]]

    expected_possible_ids = [1,2,5]
    expected_sum = 8
    print("Possible game IDs:", possible_ids)

    assert possible_ids == expected_possible_ids
    assert sum(possible_ids) == expected_sum


def test_part1_solution(problem_input):
    constraint = (12, 13, 14)
    result = [(g["game_id"], is_game_possible(g, constraint)) for g in problem_input]
    possible_ids = [r[0] for r in result if r[1]]

    expected_sum = 2776
    print("Part 1 solution:", sum(possible_ids))

    assert sum(possible_ids) == expected_sum

# Part 2


def test_p2_example(ex1_input):
    results = [fewest_cubes_possible(game) for game in ex1_input]
    solution = sum([prod(result) for result in results])

    expected_results = [(4, 2, 6), (1, 3, 4), (20, 13, 6), (14, 3, 15), (6, 3, 2)]
    expected_powers = [prod(result) for result in expected_results]
    expected_solution = sum(expected_powers)
    print("Results:", results)
    print("Powers:", expected_powers)
    print("Solution:", expected_solution)

    assert results == expected_results
    assert solution == expected_solution


def test_p2_solution(problem_input):
    results = [fewest_cubes_possible(game) for game in problem_input]
    solution = sum([prod(result) for result in results])

    accepted_solution = 68638
    print("Part 2 Solution:", solution)

    assert solution == accepted_solution