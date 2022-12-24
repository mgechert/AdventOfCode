import pytest

from aoc_utils import parse_input_file
from day12 import shortest_path, find_adjacent_nodes


@pytest.fixture
def example_input():
    matrix = parse_input_file("day12ex.txt",
                              parse_line=lambda line: list(line.strip()))

    return matrix


def test_example_input_formatted_as_expected(example_input):
    assert type(example_input) is list
    assert len(example_input) == 5
    assert len(example_input[0]) == 8
    assert example_input[0] == ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm']


def test_example_input_find_adjacent_from_start(example_input):
    adjacent_nodes = find_adjacent_nodes(example_input, 0, 0)

    expected_adjacent_nodes = [(0, 1), (1, 0)]
    print(f"Start at (0, 0) {example_input[0][0]}")
    for r, c in adjacent_nodes:
        print(f"{r},{c}: {example_input[r][c]}")

    assert adjacent_nodes == expected_adjacent_nodes


def test_example_input_find_adjacent_from_middle(example_input):
    adjacent_nodes = find_adjacent_nodes(example_input, 2, 2)

    expected_adjacent_nodes = [(0, 1), (1, 0)]
    print(f"Start at (2, 2) {example_input[2][2]}")
    for r, c in adjacent_nodes:
        print(f"{r},{c}: {example_input[r][c]}")

    assert adjacent_nodes == expected_adjacent_nodes


@pytest.mark.skip
def test_example_input_calculates_expected_path(example_input):
    path = shortest_path(example_input)

    print(path.pq)

    pytest.fail()
