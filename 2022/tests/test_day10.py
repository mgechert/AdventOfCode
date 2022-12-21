import pytest

from aoc_utils import parse_input_file
from day10 import CrtCpu


def parse_line(line):
    instruction = line.strip().split()
    if len(instruction) == 1:
        return instruction
    else:
        return (instruction[0], int(instruction[1]))


@pytest.fixture
def sample_program():
    program = [
        ('noop',),
        ('addx', 3),
        ('addx', -5),
    ]

    return program


@pytest.fixture
def example_input():
    return parse_input_file("day10ex.txt", parse_line)


@pytest.fixture
def puzzle_input():
    return parse_input_file("day10.txt", parse_line)


def test_sample_program(sample_program):
    cpu = CrtCpu()
    cpu.execute_program(sample_program)

    expected_history = [1, 1, 1, 4, 4, -1]
    print(cpu.register_history)

    assert cpu.register_history == expected_history


def test_example_input_read_correctly(example_input):
    assert type(example_input) is list
    assert len(example_input) == 146
    assert example_input[0] == ('addx', 15)


def test_puzzle_input_read_correctly(puzzle_input):
    assert type(puzzle_input) is list
    assert len(puzzle_input) == 144
    assert puzzle_input[0] == ('addx', 1)


def test_example_input_creates_expected_history(example_input):
    cpu = CrtCpu()
    cpu.execute_program(example_input)
    actual_solution = cpu.get_signal_strength()

    # Expected history values from example text - value BEFORE cycle start
    expected_history = {
        20: 21,
        60: 19,
        100: 18,
        140: 21,
        180: 16,
        220: 18
    }

    expected_solution = 13140

    for i, expected_hist in expected_history.items():
        # Note - use index i - 1 since we want the value BEFORE the cycle
        actual_history = cpu.register_history[i-1]
        print(f"{i}: expected {expected_hist}, actual {actual_history}")
        assert expected_hist == actual_history

    print(f"Length of history is {len(cpu.register_history)}")

    assert expected_solution == actual_solution


def test_part1_solution(puzzle_input):
    cpu = CrtCpu()
    cpu.execute_program(puzzle_input)
    solution = cpu.get_signal_strength()

    print(f"Part 1 solution: {solution}")

    # Accepted part 1 solution
    assert solution == 13060

# Part 2


def test_sample_input_initializes_expected_display(example_input):
    cpu = CrtCpu()
    cpu.execute_program(example_input)

    height = len(cpu.display)
    width = len(cpu.display[0])

    print(f"Display dimensions {height}H x {width}W")

    assert (height, width) == (6, 40)


def test_sample_input_draws_expected(example_input):
    cpu = CrtCpu()
    cpu.execute_program(example_input)
    cpu.draw_display()

    first_row = ''.join(cpu.display[0])
    print(first_row)

    expected_first_row = '##..##..##..##..##..##..##..##..##..##..'

    # Will not be shown when tests pass; use pytest.fail or run pytest -s
    cpu.print_display()

    # pytest.fail()
    assert first_row == expected_first_row


def test_part2_solution(puzzle_input):
    cpu = CrtCpu()
    cpu.execute_program(puzzle_input)
    cpu.draw_display(blank_char=' ')

    print("Part 2 solution")
    cpu.print_display()

    # Visual solution. Uncomment line below to deliberately fail & show output
    # pytest.fail()
    assert True
