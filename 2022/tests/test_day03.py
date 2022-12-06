import pytest

from aoc_utils import input_file_to_str_list
from day03 import calculate_rucksack_priority, calculate_group_priority


@pytest.fixture
def example_input():
    return input_file_to_str_list("day03ex.txt")


@pytest.fixture
def puzzle_input():
    return input_file_to_str_list("day03.txt")


def test_example_input_reads_six_lines(example_input):
    assert type(example_input) is list
    assert len(example_input) == 6


def test_single_priority_calculates_correctly(example_input):
    priority = calculate_rucksack_priority(example_input[0])

    assert priority == 16


def test_example_total_priority_calculates_correctly(example_input):
    total_priority = 0
    for rucksack in example_input:
        total_priority = total_priority + calculate_rucksack_priority(rucksack)

    assert total_priority == 157


def test_part1_solution(puzzle_input):
    total_priority = 0
    for rucksack in puzzle_input:
        total_priority = total_priority + calculate_rucksack_priority(rucksack)

    print(f"Part 1 solution is {total_priority}")

    # Accepted part 1 solution
    assert total_priority == 7831


# Part 2


def test_group_priority_raises_on_wrong_input_len():
    illegal_input = ['abcabc', 'cdecde']
    with pytest.raises(ValueError):
        calculate_group_priority(illegal_input)


def test_group_priority_raises_when_no_common_items():
    illegal_input = ['aa', 'bb', 'cc']  # No items in common
    with pytest.raises(ValueError):
        calculate_group_priority(illegal_input)


def test_group_priority_raises_when_multiple_common_items():
    illegal_input = ['abc', 'abe', 'abd']  # Multiple items in common
    with pytest.raises(ValueError):
        calculate_group_priority(illegal_input)


def test_example_group1_priority_calculates_correctly(example_input):
    group_rucksacks = example_input[:3]
    priority = calculate_group_priority(group_rucksacks)

    assert priority == 18


def test_example_group2_priority_calculates_correctly(example_input):
    group_rucksacks = example_input[3:]
    priority = calculate_group_priority(group_rucksacks)

    assert priority == 52


def test_example_priority_calculates_correctly(example_input):
    total_priority = 0
    for i in range(0, len(example_input), 3):
        group_priority = calculate_group_priority(example_input[i:i+3])
        total_priority = total_priority + group_priority

    assert total_priority == 70


def test_part2_solution(puzzle_input):
    total_priority = 0
    for i in range(0, len(puzzle_input), 3):
        group_priority = calculate_group_priority(puzzle_input[i:i+3])
        total_priority = total_priority + group_priority

    print(f"Part 2 solution: {total_priority}")

    # Accepted solution
    assert total_priority == 2683
