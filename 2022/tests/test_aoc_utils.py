import pytest

from aoc_utils import input_file_to_str_list


def test_input_file_to_str_list_reads_file():
    input = input_file_to_str_list("day03ex.txt")

    print(input[0])

    assert type(input) is list
    assert len(input) == 6
    assert input[0] == "vJrwpWtwJgWrhcsFMMfFFhFp"
