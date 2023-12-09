import logging
import pytest

from aoc_utils import parse_input_file
from day04 import CardScanner


@pytest.fixture
def ex1_input():
    return parse_input_file("day04ex.txt")


@pytest.fixture
def problem_input():
    return parse_input_file("day04.txt")

def test_read_inputs(ex1_input, problem_input):
    # Sanity check - did the inputs get completely read?
    ex_len = len(ex1_input)
    in_len = len(problem_input)

    expected_ex_len = 6
    expected_in_len = 215

    assert ex_len == expected_ex_len
    assert in_len == expected_in_len


def test_card_scanner_calculates_score():
    winning_nums = ["41", "48", "83", "86", "17"]
    drawn_nums = ["83", "86", "6", "31", "17", "9", "48", "53"]
    card_score, _ = CardScanner.calculate_card_score(winning_nums, drawn_nums)

    expected_score = 8

    assert card_score == expected_score


def test_card_scanner_reads_card_correctly():
    card_str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
    card = CardScanner.parse_card_str(card_str)

    expected_card_no = 1
    expected_card_score = 8
    expected_winning_nums = ["41", "48", "83", "86", "17"]
    expected_drawn_nums = ["83", "86", "6", "31", "17", "9", "48", "53"]
    print(card)

    assert card[0] == expected_card_no
    assert card[1] == expected_card_score
    assert card[2] == expected_winning_nums
    assert card[3] == expected_drawn_nums


def test_card_scanner_reads_ex1_input(ex1_input):
    card_scanner = CardScanner(ex1_input)
    card_scores = [card[1] for card in card_scanner.cards]

    expected_len = 6
    expected_scores = [8, 2, 2, 1, 0, 0]
    expected_sum = 13
    print(card_scanner.cards)

    assert len(card_scanner.cards) == expected_len
    assert card_scores == expected_scores
    assert sum(card_scores) == expected_sum


def test_part1_solution(problem_input):
    card_scanner = CardScanner(problem_input)
    card_scores = [card[1] for card in card_scanner.cards]
    total_score = sum(card_scores)

    accepted_score = 27845
    print(f"Part 1 solution: {total_score}")

    assert total_score == accepted_score


# Part 2


def test_card_scanner_calculates_winning_num_counts(ex1_input):
    card_scanner = CardScanner(ex1_input)
    winning_num_counts = [card[4] for card in card_scanner.cards]

    expected_counts = [4, 2, 2, 1, 0, 0]

    assert winning_num_counts == expected_counts


def test_part2_ex(ex1_input):
    card_scanner = CardScanner(ex1_input)
    total_cards = card_scanner.calculate_total_cards()

    expected_total_cards = 30

    assert total_cards == expected_total_cards


def test_part2_solution(problem_input):
    card_scanner = CardScanner(problem_input)
    total_cards = card_scanner.calculate_total_cards()

    accepted_solution = 9496801
    print(f"Part 2 solution: {total_cards}")

    assert total_cards == accepted_solution
