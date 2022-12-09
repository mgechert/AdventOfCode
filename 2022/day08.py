from itertools import product
from typing import List

# Advent of Code Day 8 solution code


def get_visible_matrix(tree_matrix: List[List[int]]) -> List[List[bool]]:
    """
    Given a matrix of tree heights of HxW, determine which trees are visible
    Returns a HxW matrix of bools corresponding to the trees at the same
    coordinates
    """
    height = len(tree_matrix)
    width = len(tree_matrix[0])
    visible_matrix = [[False for _ in range(width)] for _ in range(height)]

    row_iterators = []

    # Scan right and left
    for row in range(height):
        row_iterators.append(product([row], range(width)))
        row_iterators.append(product([row], range(width-1, -1, -1)))

    # Scan up and down
    for col in range(width):
        row_iterators.append(product(range(height), [col]))
        row_iterators.append(product(range(height-1, -1, -1), [col]))

    # Iterate each row (up/down/right/left)
    for row in row_iterators:
        max_height = -1

        for r, c in row:
            if tree_matrix[r][c] > max_height:
                max_height = tree_matrix[r][c]
                visible_matrix[r][c] = True

    return visible_matrix


def count_visible(visible_matrix: List[List[bool]]) -> int:
    """Counts the True values in the visible matrix"""
    height = len(visible_matrix)
    width = len(visible_matrix[0])
    visible_count = 0

    for r, c in product(range(height), range(width)):
        if visible_matrix[r][c]:
            visible_count += 1

    return visible_count
