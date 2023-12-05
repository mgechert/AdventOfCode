import pytest

from aoc_utils import parse_input_file
from day01 import calibrate_line, calibrate_document, Trie, scan_document


@pytest.fixture
def example_input():
    return parse_input_file("day01ex.txt")


@pytest.fixture
def problem_input():
    return parse_input_file("day01.txt")


def test_example_reads_as_expected(example_input):
    actual_len = len(example_input)
    expected_len = 4

    assert type(example_input) is list
    assert actual_len == expected_len


def test_problem_input_is_expected_len(problem_input):
    actual_len = len(problem_input)
    expected_len = 1000

    assert type(problem_input) is list
    assert actual_len == expected_len


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


def test_problem_input(problem_input):
    part1_solution = calibrate_document(problem_input)
    expected_solution = 54634  # Accepted p1 solution

    print(f"Part 1 solution: {part1_solution}")

    assert part1_solution == expected_solution


# Part 2
@pytest.fixture
def ex2_input():
    ex2_input = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    return ex2_input


def test_trie_basic_insert_and_search():
    trie = Trie()

    test_words = ["six", "sixteen", "sixty", "seven"]
    for word in test_words:
        trie.insert(word)

    for word in test_words:
        result = trie.search(word)

        print(f"Searched for {word} got {result}")
        assert result == word

    expected_none = trie.search("notintrie")

    assert expected_none is None


def test_trie_find_all():
    trie = Trie()
    test_words = ["six", "sixteen", "sixty", "seven"]
    for word in test_words:
        trie.insert(word)

    results = trie.find_all("sixteenthenseventhensix")

    expected_results = ["sixteen", "seven", "six"]

    assert results == expected_results


def test_scan_document_handles_examples(ex2_input):
    ex_results = scan_document(ex2_input)
    ex_sum = sum(ex_results)

    expected_values = [29, 83, 13, 24, 42, 14, 76]
    expected_sum = 281

    assert ex_results == expected_values
    assert ex_sum == expected_sum


def test_scan_document_handles_edge_case():
    """Test a fix for this edge case found in the problem input:
    szsvltgsc1onecccbfour3oneightfh
    (Was returning 11 instead of 18)
    """
    result = scan_document(["szsvltgsc1onecccbfour3oneightfh"])

    expected_result = [18]

    assert result == expected_result


def test_part2_input(problem_input):
    part2_result = scan_document(problem_input)
    part2_solution = sum(part2_result)

    for i in range(100):
        print(f"{problem_input[i]}: {part2_result[i]}")

    # Tried: 53846 (low)
    accepted_solution = 53855  # Accepted p2 solution

    print(f"Part 2 solution: {part2_solution}")

    assert part2_solution == accepted_solution
