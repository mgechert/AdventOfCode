from itertools import product
from typing import Iterable, List

# Advent of Code Day 8 solution code


def get_row_iterators(height: int, width: int) -> List[Iterable]:
    """
    Returns a list of iterators containing (r, c) coordinates over each row
    in a matrix of size height x width going left to right and right
    to left, as well as each column going top to bottom and bottom to top.
    """
    row_iterators = []

    # Scan right and left
    for row in range(height):
        row_iterators.append(product([row], range(width)))
        row_iterators.append(product([row], range(width-1, -1, -1)))

    # Scan up and down
    for col in range(width):
        row_iterators.append(product(range(height), [col]))
        row_iterators.append(product(range(height-1, -1, -1), [col]))

    return row_iterators


def get_visible_matrix(tree_matrix: List[List[int]]) -> List[List[bool]]:
    """
    Given a matrix of tree heights of HxW, determine which trees are visible
    Returns a HxW matrix of bools corresponding to the trees at the same
    coordinates
    """
    height = len(tree_matrix)
    width = len(tree_matrix[0])
    row_iterators = get_row_iterators(height, width)
    visible_matrix = [[False for _ in range(width)] for _ in range(height)]

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


def get_scenic_matrix(tree_matrix: List[List[int]]) -> List[List[int]]:
    """
    Given a matrix of tree heights of HxW, determine the "scenic score" for
    the tree at each location in the matrix.
    Returns a HxW matrix of ints corresponding to the trees at the same
    coordinates
    """
    height = len(tree_matrix)
    width = len(tree_matrix[0])
    max_height = 10  # Technically it's 9, but zero-indexed
    row_iterators = get_row_iterators(height, width)
    scenic_matrix = [[1 for _ in range(width)] for _ in range(height)]

    # Iterate each row (up/down/right/left)
    for row in row_iterators:
        next_score_for_height = [0 for _ in range(max_height)]

        for r, c in row:
            this_height = tree_matrix[r][c]
            scenic_matrix[r][c] *= next_score_for_height[this_height]

            for height in range(max_height):
                if height > this_height:
                    next_score_for_height[height] += 1
                else:
                    next_score_for_height[height] = 1

    return scenic_matrix


def matrix_max(scenic_matrix: List[List[int]]) -> int:
    """Finds max value in a 2D matrix"""
    height = len(scenic_matrix)
    width = len(scenic_matrix[0])
    max_score = 0

    for r, c in product(range(height), range(width)):
        max_score = max(scenic_matrix[r][c], max_score)

    return max_score
