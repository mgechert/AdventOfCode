import pytest
import re
from typing import Tuple

from aoc_utils import parse_input_file
from day04 import range_contains_range, range_overlaps_range


def parser(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Input in the format: A-B,C-D for two ranges A-B and C-D where
    A, B, C, and D are all ints.
    Returns: ((A, B), (C, D))
    """
    points = [int(point) for point in re.split(r'[-,]', line.strip())]

    return ((points[0], points[1]), (points[2], points[3]))


@pytest.fixture
def example_input():
    return parse_input_file("day04ex.txt", parser)


@pytest.fixture
def puzzle_input():
    return parse_input_file("day04.txt", parser)


def test_example_input_contains_expected_data(example_input):
    assert type(example_input) is list
    assert len(example_input) == 6
    assert example_input[0] == ((2, 4), (6, 8))


def test_example1_is_contained():
    range1, range2 = (2, 8), (3, 7)

    assert range_contains_range(range1, range2) is True
    assert range_contains_range(range2, range1) is True


def test_example2_is_not_contained():
    range1, range2 = (2, 4), (6, 8)

    assert range_contains_range(range1, range2) is False
    assert range_contains_range(range2, range1) is False


def test_example_has_2_contained_ranges(example_input):
    total_contained = 0

    for range1, range2 in example_input:
        if range_contains_range(range1, range2):
            total_contained = total_contained + 1

    assert total_contained == 2


def test_puzzle_input_is_expected_length(puzzle_input):
    assert len(puzzle_input) == 1000


def test_part1_solution(puzzle_input):
    total_contained = 0

    for range1, range2 in puzzle_input:
        if range_contains_range(range1, range2):
            total_contained = total_contained + 1

    print(f"Part 1 solution is: {total_contained}")

    # Accepted solution to part 1
    assert total_contained == 582


# Part 2

def test_example1_overlaps():
    range1, range2 = (5, 7), (7, 9)

    assert range_overlaps_range(range1, range2) is True
    assert range_overlaps_range(range2, range1) is True


def test_example2_does_not_overlap():
    range1, range2 = (2, 4), (6, 8)

    assert range_overlaps_range(range1, range2) is False
    assert range_overlaps_range(range2, range1) is False


def test_example_has_4_overlapping_ranges(example_input):
    total_overlapping = 0

    for range1, range2 in example_input:
        if range_overlaps_range(range1, range2):
            print(f"{range1} overlaps {range2}")
            total_overlapping = total_overlapping + 1
        else:
            print(f"{range1} does not overlap {range2}")

    assert total_overlapping == 4


def test_part2_solution(puzzle_input):
    total_overlapping = 0

    for range1, range2 in puzzle_input:
        if range_overlaps_range(range1, range2):
            total_overlapping = total_overlapping + 1

    print(f"Part 2 solution is: {total_overlapping}")

    # Accepted part 2 solution
    assert total_overlapping == 893
