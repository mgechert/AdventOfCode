import pytest
from typing import Tuple

from aoc_utils import parse_input_file
from day09 import Rope, LongRope


def parse_line(line: str) -> Tuple[str, int]:
    direction, steps = line.strip().split()

    return (direction, int(steps))


@pytest.fixture
def example_input():
    return parse_input_file("day09ex.txt", parse_line)


@pytest.fixture
def example2_input():
    return parse_input_file("day09ex2.txt", parse_line)


@pytest.fixture
def puzzle_input():
    return parse_input_file("day09.txt", parse_line)


def test_example_input_expected_output(example_input):
    direction, steps = example_input[0]

    assert type(example_input) is list
    assert len(example_input) == 8
    assert direction == 'R'
    assert steps == 4


def test_example2_input_expected_output(example2_input):
    direction, steps = example2_input[0]

    assert type(example2_input) is list
    assert len(example2_input) == 8
    assert direction == 'R'
    assert steps == 5


def test_puzzle_input_expected_output(puzzle_input):
    direction, steps = puzzle_input[0]

    assert type(puzzle_input) is list
    assert len(puzzle_input) == 2000
    assert direction == 'R'
    assert steps == 1


def test_rope_init_as_expected():
    rope = Rope()

    print(rope.tail_visited)

    assert rope.head == (0, 0)
    assert rope.tail == (0, 0)
    assert (0, 0) in rope.tail_visited


def test_rope_move_head_updates_head_state():
    rope = Rope()
    rope.move_head(dx=1, dy=0)

    assert rope.head == (1, 0)


def test_rope_move_head_fails_to_move_by_2():
    rope = Rope()

    with pytest.raises(ValueError):
        rope.move_head(dx=2, dy=0)


def test_rope_move_head_fails_to_move_both_x_and_y():
    rope = Rope()

    with pytest.raises(ValueError):
        rope.move_head(dx=2, dy=2)


def test_rope_update_tail_position_updates_tail_state():
    rope = Rope()
    new_position = (2, -2)
    rope.update_tail_position(*new_position)

    assert rope.tail == new_position
    assert new_position in rope.tail_visited
    assert len(rope.tail_visited) == 2


def test_rope_move_head_r2_moves_tail_r1():
    rope = Rope()
    rope.move(direction='R', steps=2)

    expected_head_position = (2, 0)
    expected_tail_position = (1, 0)

    assert rope.head == expected_head_position
    assert rope.tail == expected_tail_position


def test_rope_move_head_u2_moves_tail_u1():
    rope = Rope()
    rope.move(direction='U', steps=2)

    expected_head_position = (0, 2)
    expected_tail_position = (0, 1)

    assert rope.head == expected_head_position
    assert rope.tail == expected_tail_position


def test_rope_move_head_r1_l1_head_tail_overlap():
    rope = Rope()
    rope.move(direction='R', steps=1)
    rope.move(direction='L', steps=1)

    expected_head_position = (0, 0)
    expected_tail_position = (0, 0)

    assert rope.head == expected_head_position
    assert rope.tail == expected_tail_position


def test_rope_move_head_u1_d1_head_tail_overlap():
    rope = Rope()
    rope.move(direction='U', steps=1)
    rope.move(direction='D', steps=1)

    expected_head_position = (0, 0)
    expected_tail_position = (0, 0)

    assert rope.head == expected_head_position
    assert rope.tail == expected_tail_position


def test_rope_move_head_u1r2_moves_tail_u1r1():
    rope = Rope()
    rope.move(direction='U', steps=1)
    rope.move(direction='R', steps=2)

    expected_head_position = (2, 1)
    expected_tail_position = (1, 1)

    assert rope.head == expected_head_position
    assert rope.tail == expected_tail_position


def test_example_input_calculates_expected(example_input):
    rope = Rope()

    for direction, steps in example_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    assert num_tail_positions == 13


def test_part1_solution(puzzle_input):
    rope = Rope()

    for direction, steps in puzzle_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    print(f"Part 1 solution is {num_tail_positions}")

    # Accepted part 1 solution
    assert num_tail_positions == 6057

# Part 2


def test_longrope_against_p1_example(example_input):
    # A LongRope with 2 knots should still produce the part 1 solution
    rope = LongRope(num_knots=2)

    for direction, steps in example_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    assert num_tail_positions == 13


def test_longrope_against_p1_solution(puzzle_input):
    # A LongRope with 2 knots should still produce the part 1 solution
    rope = LongRope(num_knots=2)

    for direction, steps in puzzle_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    assert num_tail_positions == 6057


def test_example_calculates_expected_p2(example_input):
    rope = LongRope()

    for direction, steps in example_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    assert num_tail_positions == 1


@pytest.mark.skip
def test_example2_calculates_expected(example2_input):
    rope = LongRope()

    for direction, steps in example2_input[:2]:
        rope.move(direction, steps)
        print(f"Move: {direction} {steps}: {rope.knots}")


    num_tail_positions = len(rope.tail_visited)

    print(rope.tail_visited)

    assert num_tail_positions == 36


@pytest.mark.skip
def test_part2_solution(puzzle_input):
    rope = LongRope()

    for direction, steps in puzzle_input:
        rope.move(direction, steps)

    num_tail_positions = len(rope.tail_visited)

    print(f"Part 2 solution is {num_tail_positions}")

    # Accepted part 1 solution
    assert num_tail_positions == 6057
