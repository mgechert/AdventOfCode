from typing import Tuple

# Advent of Code Day 4 solution code


def range_contains_range(range1: Tuple[int, int],
                         range2: Tuple[int, int]) -> bool:
    """Returns True if either range completely contains the other"""

    start1, end1 = range1
    start2, end2 = range2

    # Does range 1 fully contain range 2?
    if start2 >= start1 and end2 <= end1:
        return True
    # Does range 2 fully contain range 1?
    elif start1 >= start2 and end1 <= end2:
        return True
    else:
        return False


def range_overlaps_range(range1: Tuple[int, int],
                         range2: Tuple[int, int]) -> bool:
    """Returns True if the ranges overlap at all"""
    start1, end1 = range1
    start2, end2 = range2

    if start1 >= start2 and start1 <= end2:
        return True
    elif end1 >= start2 and end1 <= end2:
        return True
    elif start2 >= start1 and start2 <= end1:
        return True
    elif end2 >= start1 and end2 <= end1:
        return True
    else:
        return False
