import pytest

from aoc_utils import parse_input_file
from day06 import find_packet_start, find_message_start


@pytest.fixture
def puzzle_input():
    """Input is 1 line only, return the string directly"""
    input = parse_input_file("day06.txt")
    assert len(input) == 1

    return input[0]


def test_puzzle_input_is_single_string(puzzle_input):
    assert type(puzzle_input) is str


def test_example1_finds_packet_start():
    packet = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    start = find_packet_start(packet)

    assert start == 7


def test_example2_finds_packet_start():
    packet = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

    start = find_packet_start(packet)

    assert start == 5


def test_example3_finds_packet_start():
    packet = 'nppdvjthqldpwncqszvftbrmjlhg'

    start = find_packet_start(packet)

    assert start == 6


def test_example4_finds_packet_start():
    packet = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

    start = find_packet_start(packet)

    assert start == 10


def test_example5_finds_packet_start():
    packet = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

    start = find_packet_start(packet)

    assert start == 11


def test_part1_solution(puzzle_input):
    start = find_packet_start(puzzle_input)

    print(f"Part 1 solution: {start}")

    # Accepted part 1 solution
    assert start == 1356


# Part 2


def test_example1_finds_message_start():
    packet = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    start = find_message_start(packet)

    assert start == 19


def test_example2_finds_message_start():
    packet = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

    start = find_message_start(packet)

    assert start == 23


def test_example3_finds_message_start():
    packet = 'nppdvjthqldpwncqszvftbrmjlhg'

    start = find_message_start(packet)

    assert start == 23


def test_example4_finds_message_start():
    packet = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

    start = find_message_start(packet)

    assert start == 29


def test_example5_finds_message_start():
    packet = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

    start = find_message_start(packet)

    assert start == 26


def test_part2_solution(puzzle_input):
    start = find_message_start(puzzle_input)

    print(f"Part 2 solution: {start}")

    # Accepted part 2 solution
    assert start == 2564
