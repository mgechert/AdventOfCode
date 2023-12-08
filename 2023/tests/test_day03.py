import pytest

from aoc_utils import parse_input_file, get_adjacent_points
from day03 import Schematic

@pytest.fixture
def ex1_input():
    ex1_input = parse_input_file("day03ex.txt")

    return ex1_input


@pytest.fixture
def problem_input():
    problem_input = parse_input_file("day03.txt")

    return problem_input


def test_read_inputs(ex1_input, problem_input):
    # Sanity check - did the inputs get completely read?
    ex_len = len(ex1_input)
    in_len = len(problem_input)

    expected_ex_len = 10
    expected_in_len = 140

    assert ex_len == expected_ex_len
    assert in_len == expected_in_len

# Tests for new util method get_adjacent_points()

def test_get_adjacent_points_returns_8_points():
    adjacent_points = get_adjacent_points(row=1, col=1, num_rows=3, num_cols=3)

    expected_points = [(0, 0), (0, 1), (0, 2),
                       (1, 0), (1, 2),
                       (2, 0), (2, 1), (2, 2)]

    assert adjacent_points == expected_points


def test_get_adjacent_points_returns_3_points_upper_left_corner():
    # (0, 0) is only adjacent to 3 points
    adjacent_points = get_adjacent_points(row=0, col=0, num_rows=3, num_cols=3)

    expected_points = [(0, 1),
                       (1, 0), (1, 1)]

    assert adjacent_points == expected_points


def test_get_adjacent_points_returns_3_points_lower_right_corner():
    # (2, 2) is only adjacent to 3 points
    adjacent_points = get_adjacent_points(row=2, col=2, num_rows=3, num_cols=3)

    expected_points = [(1, 1), (1, 2),
                       (2, 1)]

    assert adjacent_points == expected_points


def test_ex1_reads_expected_partnums(ex1_input):
    schematic = Schematic(ex1_input)
    partnums = [partnum for (partnum, _) in schematic.partnum_coords]

    expected_partnums = [467, 114, 35, 633, 617, 58, 592, 755, 664, 598]

    assert partnums == expected_partnums


def test_ex1_validates_expected_partnums(ex1_input):
    schematic = Schematic(ex1_input)
    valid_partnums = schematic.valid_partnums

    expected_partnums = [467, 35, 633, 617, 592, 755, 664, 598]
    expected_sum = 4361

    assert valid_partnums == expected_partnums
    assert sum(valid_partnums) == expected_sum


def test_p1_solution(problem_input):
    schematic = Schematic(problem_input)
    valid_partnums = schematic.valid_partnums
    solution = sum(valid_partnums)

    # Tried 8 261 382 (too high)
    accepted_solution = 532331
    print(f"Part 1 solution: {solution}")
    
    assert solution == accepted_solution


# Part 2


def test_schematic_locates_gears(ex1_input):
    schematic = Schematic(ex1_input)
    gear_coords = schematic.gear_coords

    expected_coords = set([(1, 3), (8, 5), (4, 3)])

    print(gear_coords)

    assert gear_coords == expected_coords


def test_schematic_calculates_expected_ex1_solution(ex1_input):
    schematic = Schematic(ex1_input)
    solution = schematic.calculate_gear_ratio_sum()

    expected_solution = 467835

    assert solution == expected_solution


def test_p2_solution(problem_input):
    schematic = Schematic(problem_input)
    solution = schematic.calculate_gear_ratio_sum()

    accepted_solution = 82301120

    print(f"Part 2 solution: {solution}")

    assert solution == accepted_solution