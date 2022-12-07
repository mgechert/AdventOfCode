# Advent of Code Day 5 solution code

class CrateShip:
    def __init__(self, stacks):
        # Put a None at index 0 so stack numbers match indices
        self.stacks = [None] + stacks

    def move_crates(self,
                    num_crates: int,
                    from_stack: int,
                    to_stack: int) -> None:
        for _ in range(num_crates):
            self.stacks[to_stack].append(self.stacks[from_stack].pop())

    def get_stacks(self):
        return self.stacks[1:]

    def get_top_row(self):
        top_row = []
        for stack in self.stacks[1:]:
            if len(stack) > 0:
                top_row.append(stack[-1])

        return ''.join(top_row)


class CrateMover(CrateShip):
    def move_crates(self,
                    num_crates: int,
                    from_stack: int,
                    to_stack: int) -> None:
        # Remove num_crates from the end of from_stack
        moving_crates = self.stacks[from_stack][-num_crates:]
        self.stacks[from_stack] = self.stacks[from_stack][:-num_crates]

        # Put the removed crates on top of to_stack
        self.stacks[to_stack] = self.stacks[to_stack] + moving_crates
