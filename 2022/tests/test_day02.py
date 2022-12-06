import os
import pytest

from day02 import read_file, score_round, score_rounds, score_rounds_2

INPUTS_PATH = os.path.join(os.path.dirname(__file__), "inputs/")


@pytest.fixture
def example_rounds():
    return read_file(f"{INPUTS_PATH}day02ex.txt")


@pytest.fixture
def puzzle_input():
    return read_file(f"{INPUTS_PATH}day02.txt")


def test_read_example_file_returns_3_rounds(example_rounds):
    assert len(example_rounds) == 3


def test_read_example_file_returns_expected_tuples(example_rounds):
    expected = [
        ('A', 'Y'),
        ('B', 'X'),
        ('C', 'Z')
    ]

    assert example_rounds == expected


def test_score_round_calculates_ex_round1(example_rounds):
    score = score_round(example_rounds[0])

    assert score == 8


def test_score_round_calculates_ex_round2(example_rounds):
    score = score_round(example_rounds[1])

    assert score == 1


def test_score_round_calculates_ex_round3(example_rounds):
    score = score_round(example_rounds[2])

    assert score == 6


def test_score_rounds_calculates_example_correctly(example_rounds):
    total_score = score_rounds(example_rounds)

    assert total_score == 15


def test_part1_input_is_correct_length(puzzle_input):
    assert type(puzzle_input) is list
    assert len(puzzle_input) == 2500


def test_part1_solution(puzzle_input):
    part1_solution = score_rounds(puzzle_input)

    print(f"Part 1 solution: {part1_solution}")

    # Accepted solution for P1
    assert part1_solution == 13484


""" Part 2"""


def test_score_rounds2_calculates_example_correctly(example_rounds):
    score = score_rounds_2(example_rounds)

    assert score == 12


def test_part_2_solution(puzzle_input):
    part2_solution = score_rounds_2(puzzle_input)

    print(f"Part 2 solution: {part2_solution}")

    # Accepted part 2 solution
    assert part2_solution == 13433
