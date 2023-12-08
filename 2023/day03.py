from aoc_utils import get_adjacent_points
from itertools import product
from typing import List

# Advent of Code Day 3 solution code

class Schematic:

    def __init__(self, input_text: List[str]) -> None:
        self.ROWS = len(input_text)
        self.COLS = len(input_text[0])
        self.valid_partnums = []
        self.gear_pairs = []

        # Every part num found and a set of points it occupies
        self.partnum_coords = []

        # A set of every point adjacent to a symbol
        self.symbol_adjacent_coords = set()

        # A set of every (r,c) where a gear ("*") is found
        self.gear_coords = set()

        for r in range(self.ROWS):
            current_partnum = ""
            current_partnum_coords = set()

            for c in range(self.COLS):
                char = input_text[r][c]
                if char in "0123456789":
                    current_partnum = current_partnum + char
                    current_partnum_coords.add((r, c))
                else:
                    if current_partnum:
                        # At a '.' or symbol add the current partnum if it we're done reading one
                        self.partnum_coords.append((int(current_partnum), current_partnum_coords))
                        current_partnum = ""
                        current_partnum_coords = set()
                    if char != ".":
                        # Handle a symbol
                        adjacent_points = get_adjacent_points(r, c, self.ROWS, self.COLS)
                        self.symbol_adjacent_coords.update(adjacent_points)

                        if char == "*":
                            self.gear_coords.add((r, c))


            if current_partnum:
                # At end of a row, add the current partnum if there is one
                self.partnum_coords.append((int(current_partnum), current_partnum_coords))

        # A partnum is valid if there is any intersection between any of the partnum's
        # (r,c) coordinates and the set of symbol-adjacent coordinates
        for (partnum, coords) in self.partnum_coords:
            if len(self.symbol_adjacent_coords.intersection(coords)) > 0:
                self.valid_partnums.append(partnum)
        
        # Find all gear pairs where a gear is adjacent to exactly 2 partnums
        for (r, c) in self.gear_coords:
            adjacent_partnums = []
            gear_adjacent = set(get_adjacent_points(r, c, self.ROWS, self.COLS))
            for (partnum, coords) in self.partnum_coords:
                if len(gear_adjacent.intersection(coords)) > 0:
                    adjacent_partnums.append(partnum)
            
            if len(adjacent_partnums) == 2:
                self.gear_pairs.append((adjacent_partnums[0], adjacent_partnums[1]))

    def calculate_gear_ratio_sum(self):
        gear_ratio_sum = 0
        for (a, b) in self.gear_pairs:
            gear_ratio_sum = gear_ratio_sum + (a * b)

        return gear_ratio_sum

