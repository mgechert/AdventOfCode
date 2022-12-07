import os
import pytest
import re
from typing import List, Tuple

from day05 import CrateShip, CrateMover

INPUTS_PATH = os.path.join(os.path.dirname(__file__), "inputs")


def parse_input_file(filename: str) -> Tuple[List[List[str]], Tuple[int, int, int]]:
    with open(f"{INPUTS_PATH}/{filename}") as f:
        # Use the length of the first line to determine how many stacks
        line = f.readline()
        num_stacks = (len(line) + 1)//4
        stacks = [[] for _ in range(num_stacks)]

        # Build stacks until reaching the line containing stack numbers
        while re.match(r'\s*\[[A-Z]\]\s*', line):
            for stack_num in range(num_stacks):
                stack_index = stack_num * 4 + 1
                if line[stack_index] != ' ':
                    stacks[stack_num].insert(0, line[stack_index])

            line = f.readline()

        _ = f.readline()  # Empty line between stacks and moves; discard
        line = f.readline()  # This should be the first move

        # Read moves
        moves = []
        while line:
            match = re.match(r'^move (\d+) from (\d+) to (\d+)', line)
            num_crates = int(match[1])
            from_stack = int(match[2])
            to_stack = int(match[3])
            moves.append((num_crates, from_stack, to_stack))
            line = f.readline()

    return stacks, moves


@pytest.fixture
def example_input():
    return parse_input_file("day05ex.txt")


@pytest.fixture
def puzzle_input():
    return parse_input_file("day05.txt")


def test_example_input_reads_3_stacks(example_input):
    stacks, _ = example_input

    expected_stacks = [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
    ]

    assert len(stacks) == 3
    assert stacks == expected_stacks


def test_example_input_reads_4_moves(example_input):
    _, moves = example_input

    expected_moves = [
        (1, 2, 1),
        (3, 1, 3),
        (2, 2, 1),
        (1, 1, 2),
    ]

    assert moves == expected_moves


def test_puzzle_input_reads_expected(puzzle_input):
    stacks, moves = puzzle_input
    num_stacks = len(stacks)
    num_moves = len(moves)

    assert num_stacks == 9
    assert num_moves == 501


def test_example_first_move_updates_stacks(example_input):
    stacks, moves = example_input
    crate_ship = CrateShip(stacks)

    # Apply the first move
    num_crates, from_stack, to_stack = moves[0]
    print(f"move {num_crates} from {from_stack} to {to_stack}")
    crate_ship.move_crates(num_crates, from_stack, to_stack)

    expected_stacks = [
        ['Z', 'N', 'D'],
        ['M', 'C'],
        ['P']
    ]

    assert crate_ship.get_stacks() == expected_stacks


def test_example_moves_match_expected_state(example_input):
    stacks, moves = example_input
    crate_ship = CrateShip(stacks)

    # Apply all moves
    for move in moves:
        crate_ship.move_crates(*move)

    expected_stacks = [
        ['C'],
        ['M'],
        ['P', 'D', 'N', 'Z']
    ]

    assert crate_ship.get_stacks() == expected_stacks


def test_example_moves_match_expected_top_row(example_input):
    stacks, moves = example_input
    crate_ship = CrateShip(stacks)

    # Apply all moves
    for move in moves:
        crate_ship.move_crates(*move)

    expected_top_row = 'CMZ'

    assert crate_ship.get_top_row() == expected_top_row


def test_part1_solution(puzzle_input):
    stacks, moves = puzzle_input
    crate_ship = CrateShip(stacks)

    for move in moves:
        crate_ship.move_crates(*move)
    top_row = crate_ship.get_top_row()

    expected_top_row = 'QNHWJVJZW'

    print(f"Part 1 solution is {top_row}")

    # Accepted part 1 solution
    assert top_row == expected_top_row

# Part 2


def test_example_state_matches_part2(example_input):
    stacks, moves = example_input
    crate_mover = CrateMover(stacks)

    # Apply all moves
    for move in moves:
        crate_mover.move_crates(*move)

    expected_stacks = [
        ['M'],
        ['C'],
        ['P', 'Z', 'N', 'D']
    ]
    expected_top_row = 'MCD'

    assert crate_mover.get_stacks() == expected_stacks
    assert crate_mover.get_top_row() == expected_top_row


def test_part2_solution(puzzle_input):
    stacks, moves = puzzle_input
    crate_mover = CrateMover(stacks)

    for move in moves:
        crate_mover.move_crates(*move)
    top_row = crate_mover.get_top_row()

    print(f"Part 2 solution is {top_row}")

    # Accepted part 2 solution
    assert top_row == 'BPCZJLFJW'
