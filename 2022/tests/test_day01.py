import os
import pytest

from day01 import split_groups, sum_groups, sum_top_k

INPUTS_PATH = os.path.join(os.path.dirname(__file__), "inputs/")


def read_file_to_str(filename):
    with open(f"{INPUTS_PATH}{filename}") as f:
        str_data = f.read()

    return str_data


@pytest.fixture
def sample_input():
    """Sample input: answer is 24000"""
    sample_input = read_file_to_str("day01ex.txt")

    return sample_input


@pytest.fixture
def puzzle_input():
    """Puzzle input"""
    puzzle_input = read_file_to_str("day01a.txt")

    return puzzle_input


def test_sample_has_five_groups(sample_input):
    ''' This list represents the Calories of the food carried by five
        Elves:
    '''
    groups = split_groups(sample_input)
    actual = len(groups)

    assert actual == 5


def test_sample_groups_contain_ints(sample_input):
    groups = split_groups(sample_input)

    for group in groups:
        assert all(type(num) is int for num in group)


def test_sample_groups_are_correct(sample_input):
    """
        The first Elf is carrying food with 1000, 2000, and 3000
        The second Elf is carrying one food item with 4000 Calories.
        The third Elf is carrying food with 5000 and 6000 Calories
        The fourth Elf is carrying food with 7000, 8000, and 9000 Calories
        The fifth Elf is carrying one food item with 10000 Calories.
    """
    groups = split_groups(sample_input)

    expected = [[1000, 2000, 3000],
                [4000],
                [5000, 6000],
                [7000, 8000, 9000],
                [10000]]

    assert groups == expected


def test_sample_totals_are_correct(sample_input):
    """
        The first Elf: total of 6000 Calories.
        The second Elf: 4000 Calories.
        The third Elf: 11000 Calories.
        The fourth Elf: 24000 Calories.
        The fifth Elf: 10000 Calories.
    """
    groups = split_groups(sample_input)
    sums = sum_groups(groups)

    expected = [6000, 4000, 11000, 24000, 10000]

    assert sums == expected


def test_sample_max_correct(sample_input):
    groups = split_groups(sample_input)
    sums = sum_groups(groups)
    max_sum = max(sums)

    assert max_sum == 24000


def test_part_1(puzzle_input):
    groups = split_groups(puzzle_input)
    sums = sum_groups(groups)
    max_sum = max(sums)

    print(f"P1 solution: {max_sum}")

    # Correct answer accepted by AOC
    assert max_sum == 70764


def test_sample_part_2(sample_input):
    groups = split_groups(sample_input)
    sums = sum_groups(groups)
    sample_top_3 = sum_top_k(sums, 3)

    assert sample_top_3 == 45000


def test_part_2(puzzle_input):
    groups = split_groups(puzzle_input)
    sums = sum_groups(groups)
    top_3 = sum_top_k(sums, 3)

    print(f"P2 solution: {top_3}")

    # accepted by AOC
    assert top_3 == 203905
