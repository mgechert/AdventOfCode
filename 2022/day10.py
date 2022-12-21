from typing import List, Tuple


class CrtCpu:
    DISPLAY_WIDTH = 40
    DISPLAY_HEIGHT = 6

    def __init__(self) -> None:
        self.register_history = [1]
        self.display = [['' for _ in range(self.DISPLAY_WIDTH)]
                        for _ in range(self.DISPLAY_HEIGHT)]

    def execute_program(self, instructions: List[Tuple[str, int]]) -> None:
        """
        Executes the given program input, appending to the register_history
        """
        for instruction in instructions:
            current_x = self.register_history[-1]

            if instruction[0] == 'addx':
                operand = instruction[1]
                self.register_history.extend([current_x, (current_x + operand)])
            elif instruction[0] == 'noop':
                self.register_history.append(current_x)
            else:
                raise ValueError(f"Illegal instruction: {instruction}")

    def get_signal_strength(self) -> None:
        """
        Calculates signal strength as defined in the problem, as the sum of
        cycle * register_at_cycle_start for cycles 20, 60, 100, 140, 180, 220
        ***Note that the register at cycle START is the value at cycle_num - 1,
        as the registry history reflects the register value at the cycle END
        """
        signal_strength = 0
        for cycle in [20, 60, 100, 140, 180, 220]:
            register = self.register_history[cycle-1]
            signal_strength += cycle * register

        return signal_strength

    def draw_display(self, blank_char: str = ".") -> None:
        """
        Calculates if the pixel should be drawn during the given cycle
        based on the current value of the x register.
        """
        # The value of the register AFTER the last cycle is executed is ignored
        for cycle_num, register in enumerate(self.register_history[:-1]):
            row = cycle_num // self.DISPLAY_WIDTH
            col = cycle_num % self.DISPLAY_WIDTH

            if abs(register - col) < 2:
                self.display[row][col] = '#'
            else:
                self.display[row][col] = blank_char

    def print_display(self) -> None:
        """Prints the display to stdout"""
        for row in range(self.DISPLAY_HEIGHT):
            print(''.join(self.display[row]))
