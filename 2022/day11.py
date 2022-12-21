from itertools import product
from typing import Callable, List, Tuple


class BarrelOfMonkeys:
    """Mediator to handle communication between monkeys"""

    def __init__(self) -> None:
        self.monkeys = []

    def throw_item(self, recipient: int, new_item: int) -> None:
        if recipient > len(self.monkeys) - 1 or recipient < 0:
            raise ValueError(f"Monkey {recipient} does not exist")

        self.monkeys[recipient].receive(new_item)

    def add_monkey(self, monkey) -> None:
        self.monkeys.append(monkey)

    def play(self,
             num_rounds: int,
             starting_monkey: int = 0,
             chatty: bool = False) -> None:
        """
        Tell each monkey in turn to take its turn, until the specified number
        of turns has been completed.
        Note: 1 round is every monkey in the barrel taking its turn
        """
        num_monkeys = len(self.monkeys)
        for _, monkey_num in product(range(num_rounds), range(num_monkeys)):
            if chatty:
                print(f"Monkey {monkey_num}:")
            self.monkeys[monkey_num].take_turn(chatty)

    def get_inspection_counts(self) -> List[int]:
        """Polls each monkey to see how many inspections they have done"""
        inspection_counts = []
        for monkey in self.monkeys:
            inspection_counts.append(monkey.inspections)

        return inspection_counts


class Monkey:
    def __init__(self,
                 starting_items: List[int],
                 operation: Callable,
                 test: Tuple[int, int, int],
                 barrel: BarrelOfMonkeys
                 ) -> None:
        """
        Initialize with specified starting items.
        operation takes a function with a single input and an int output
        test takes a tuple of length 3 containing the test condition, the
            recipient # when the condition is true, and recipient # when false
        barrel takes a reference to the "parent" barrel used to communicate w
            other Monkey objects
        """
        self.items = starting_items
        self.operation = operation
        self.test_condition, self.test_true, self.test_false = test
        self.barrel = barrel
        self.reduce_level = True  # When True, divides worry level by 3 each turn
        self.inspections = 0

    def take_turn(self, chatty=False) -> None:
        """Inspect every item in the items queue"""
        while len(self.items) > 0:
            self.inspections += 1
            current_item = self.items.pop(0)
            modified_item = self.operation(current_item)

            reduced_item = modified_item // 3 if self.reduce_level else modified_item
            recipient = self._test(reduced_item)
            self.barrel.throw_item(recipient, reduced_item)

            if chatty:
                print(f"  Inspect item: {current_item}")
                print(f"    Worry level modified to {modified_item}")
                if self.reduce_level:
                    print(f"    Worry level divided by 3 to {reduced_item}")
                print(f"    Item {reduced_item} thrown to monkey {recipient}")
    
    def _test(self, item: int) -> int:
        """
        Performs this monkey's modulo test against the specified item value
        and returns the appropriate recipient number
        """
        if item % self.test_condition == 0:
            return self.test_true
        else:
            return self.test_false

            



    def receive(self, item: int) -> None:
        """Catch an item from another monkey"""
        self.items.append(item)
