import pytest

from day11 import BarrelOfMonkeys, Monkey


@pytest.fixture
def example_input():
    barrel = BarrelOfMonkeys()
    # Monkey 0
    barrel.add_monkey(Monkey(
            starting_items=[79, 98],
            operation=lambda old: old * 19,
            test=(23, 2, 3),
            barrel=barrel
        )
    )
    # Monkey 1
    barrel.add_monkey(Monkey(
            starting_items=[54, 65, 75, 74],
            operation=lambda old: old + 6,
            test=(19, 2, 0),
            barrel=barrel
        )
    )
    # Monkey 2
    barrel.add_monkey(Monkey(
            starting_items=[79, 60, 97],
            operation=lambda old: old * old,
            test=(13, 1, 3),
            barrel=barrel
        )
    )
    # Monkey 3
    barrel.add_monkey(Monkey(
            starting_items=[74],
            operation=lambda old: old + 3,
            test=(17, 0, 1),
            barrel=barrel
        )
    )

    return barrel


@pytest.fixture
def puzzle_input():
    barrel = BarrelOfMonkeys()
    # Monkey 0
    barrel.add_monkey(Monkey(
            starting_items=[50, 70, 54, 83, 52, 78],
            operation=lambda old: old * 3,
            test=(11, 2, 7),
            barrel=barrel
        )
    )
    # Monkey 1
    barrel.add_monkey(Monkey(
            starting_items=[71, 52, 58, 60, 71],
            operation=lambda old: old * old,
            test=(7, 0, 2),
            barrel=barrel
        )
    )
    # Monkey 2
    barrel.add_monkey(Monkey(
            starting_items=[66, 56, 56, 94, 60, 86, 73],
            operation=lambda old: old + 1,
            test=(3, 7, 5),
            barrel=barrel
        )
    )
    # Monkey 3
    barrel.add_monkey(Monkey(
            starting_items=[83, 99],
            operation=lambda old: old + 8,
            test=(5, 6, 4),
            barrel=barrel
        )
    )
    # Monkey 4
    barrel.add_monkey(Monkey(
            starting_items=[98, 98, 79],
            operation=lambda old: old + 3,
            test=(17, 1, 0),
            barrel=barrel
        )
    )
    # Monkey 5
    barrel.add_monkey(Monkey(
            starting_items=[76],
            operation=lambda old: old + 4,
            test=(13, 6, 3),
            barrel=barrel
        )
    )
    # Monkey 6
    barrel.add_monkey(Monkey(
            starting_items=[52, 51, 84, 54],
            operation=lambda old: old * 17,
            test=(19, 4, 1),
            barrel=barrel
        )
    )
    # Monkey 7
    barrel.add_monkey(Monkey(
            starting_items=[82, 86, 91, 79, 94, 92, 59, 94],
            operation=lambda old: old + 7,
            test=(2, 5, 3),
            barrel=barrel
        )
    )

    return barrel


def test_barrel_throw_raises_valueerror_when_throw_to_non_monkey(example_input):
    barrel = example_input

    with pytest.raises(ValueError):
        barrel.throw_item(recipient=4, new_item=1)


def test_monkey_receive_item_adds_item(example_input):
    monkey = example_input.monkeys[0]
    monkey.receive(item=99)

    assert monkey.items[-1] == 99


def test_monkey_turn_updates_items_as_expected(example_input):
    monkey0 = example_input.monkeys[0]
    monkey0.take_turn(chatty=True)

    monkey3 = example_input.monkeys[3]

    assert monkey0.inspections == 2
    assert len(monkey0.items) == 0
    assert monkey3.items[-2:] == [500, 620]


def test_barrel_play_turn_updates_items_as_expected(example_input):
    barrel = example_input
    barrel.play(num_rounds=1, chatty=True)

    monkey0 = example_input.monkeys[0]
    monkey1 = example_input.monkeys[1]

    monkey0_expected_items = [20, 23, 27, 26]
    monkey1_expected_items = [2080, 25, 167, 207, 401, 1046]

    print("After round 1:")
    print(f"Monkey 0: {monkey0.items}")
    print(f"Monkey 1: {monkey1.items}")

    assert monkey0.items == monkey0_expected_items
    assert monkey1.items == monkey1_expected_items


def test_example_input_20_turns_has_expected_state(example_input):
    barrel = example_input
    barrel.play(num_rounds=20, chatty=True)
    inspection_counts = barrel.get_inspection_counts()

    expected_counts = [101, 95, 7, 105]
    print(f"Inspection counts: {inspection_counts}")

    assert inspection_counts == expected_counts


def test_example_input_calculates_expected_solution(example_input):
    barrel = example_input
    barrel.play(num_rounds=20)
    inspection_counts = barrel.get_inspection_counts()

    most_act1, most_act2 = sorted(inspection_counts, reverse=True)[:2]
    solution = most_act1 * most_act2
    print(f"Example solution: {solution}")

    expected_solution = 10605

    assert solution == expected_solution


def test_part1_solution(puzzle_input):
    barrel = puzzle_input
    barrel.play(num_rounds=20)
    inspection_counts = barrel.get_inspection_counts()

    most_act1, most_act2 = sorted(inspection_counts, reverse=True)[:2]
    solution = most_act1 * most_act2
    print(f"Part 1 solution: {solution}")

    # Accepted part 1 solution
    expected_solution = 102399

    assert solution == expected_solution

# Part 2


@pytest.fixture
def example2_input(example_input):
    """Modify example monkeys to not divide items by 3 on each turn"""
    barrel = example_input
    for monkey in barrel.monkeys:
        monkey.reduce_level = False

    return barrel


@pytest.fixture
def puzzle2_input(puzzle_input):
    """Modify monkeys from part 1 to not divide items by 3 on each turn"""
    barrel = puzzle_input
    for monkey in barrel.monkeys:
        monkey.reduce_level = False

    return barrel

@pytest.mark.skip
def test_example2_input_calculates_expected_solution(example2_input):
    barrel = example2_input
    barrel.play(num_rounds=1000)
    inspection_counts = barrel.get_inspection_counts()

    most_act1, most_act2 = sorted(inspection_counts, reverse=True)[:2]
    solution = most_act1 * most_act2
    print(f"Example solution: {solution}")
    print(f"Inspection counts: {inspection_counts}")

    pytest.fail()
    # expected_solution = 0

    #assert solution == expected_solution