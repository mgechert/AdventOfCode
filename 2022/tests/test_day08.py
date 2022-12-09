import pytest

from aoc_utils import parse_input_file
from day08 import get_visible_matrix, count_visible


def parse_line(line):
    return [int(i) for i in line.strip()]


@pytest.fixture
def example_input():
    return parse_input_file("day08ex.txt", parse_line)


@pytest.fixture
def puzzle_input():
    return parse_input_file("day08.txt", parse_line)


def test_example_input_is_correct_type(example_input):
    print(example_input)

    assert type(example_input) is list
    assert len(example_input) == 5
    assert type(example_input[0]) is list
    assert len(example_input[0]) == 5


def test_example_visible_matrix_returns_expected(example_input):
    visible_matrix = get_visible_matrix(example_input)
    visible_count = count_visible(visible_matrix)

    print(visible_matrix)
    print(f"{visible_count} trees are visible")

    assert visible_count == 21


def test_part1_solution(puzzle_input):
    visible_matrix = get_visible_matrix(puzzle_input)
    visible_count = count_visible(visible_matrix)

    print(f"Part 1 solution is {visible_count}")

    # Accepted part 1 solution
    assert visible_count == 1812
