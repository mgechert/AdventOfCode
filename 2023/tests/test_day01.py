import pytest

from aoc_utils import parse_input_file
from day01 import calibrate_line, calibrate_document, calibrate_line_v2


@pytest.fixture
def example_input():
    return parse_input_file("day01ex.txt")

@pytest.fixture
def part1_input():
    return parse_input_file("day01.txt")


def test_example_reads_as_expected(example_input):
    actual_len = len(example_input)
    expected_len = 4

    assert type(example_input) is list
    assert actual_len == expected_len


def test_part1_input_is_expected_len(part1_input):
    actual_len = len(part1_input)
    expected_len = 1000

    assert type(part1_input) is list
    assert actual_len == expected_len


def test_calibrate_line_reads_line_with_2_digits():
    value = calibrate_line("1abc2")
    expected_value = 12

    assert value == expected_value


def test_calibrate_line_reads_line_with_2_digits():
    value = calibrate_line("1abc2")
    expected_value = 12

    assert value == expected_value


def test_calibrate_line_reads_line_with_1_digit():
    value = calibrate_line("treb7uchet")
    expected_value = 77

    assert value == expected_value


def test_calibrate_line_reads_line_with_many_digits():
    value = calibrate_line("a1b2c3d4e5f")
    expected_value = 15

    assert value == expected_value


def test_calibrate_line_raises_value_error_when_no_digits():
    no_digit_line = "nodigits"
    with pytest.raises(ValueError):
        _ = calibrate_line(no_digit_line)


def test_calibrate_example_document_returns_expected(example_input):
    example_solution = calibrate_document(example_input)
    expected_solution = 142

    assert example_solution == expected_solution


def test_part1_input(part1_input):
    part1_solution = calibrate_document(part1_input)
    expected_solution = 54634  # Accepted p1 solution

    print(f"Part 1 solution: {part1_solution}")

    assert part1_solution == expected_solution


# Part 2
def test_format_line_handles_examples():
    ex2_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]
    ex_values = [calibrate_line_v2(line) for line in ex2_input]

    expected_values = [29, 83, 13, 24, 42, 14, 76]

    assert ex_values == expected_values
