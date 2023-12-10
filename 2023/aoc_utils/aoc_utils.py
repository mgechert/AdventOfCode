import os
from typing import Any, Callable, List, Tuple


def parse_input_file(filename: str,
                     parse_line: Callable = lambda line: line.strip(),
                     inputs_path: str = None) -> List[Any]:
    """
    Read the given input file into a list, applying the optional
    parse_fn
    """
    inputs_path = inputs_path or os.environ.get("AOC_INPUTS_PATH", None)
    if not inputs_path:
        raise EnvironmentError("AOC_INPUTS_PATH not set in os.environ,"
                               "and inputs_path was not explicitly specified")
    output = []

    with open(f"{inputs_path}/{filename}") as f:
        for line in f.readlines():
            output.append(parse_line(line))

    return output



def read_raw_input_file(filename: str,
                     inputs_path: str = None) -> str:
    """
    Read the given input file into a single string
    """
    inputs_path = inputs_path or os.environ.get("AOC_INPUTS_PATH", None)
    if not inputs_path:
        raise EnvironmentError("AOC_INPUTS_PATH not set in os.environ,"
                               "and inputs_path was not explicitly specified")

    with open(f"{inputs_path}/{filename}") as f:
        output = f.read()

    return output


def get_adjacent_points(row: int, col: int, num_rows: int, num_cols: int) -> List[Tuple[int, int]]:
    """Given a point (r, c), return a list of up to 8 adjacent points based on a
        2D array of size num_rows x num_cols, filtering out indices that would be
        out-of-bounds. (Recall that my_list[-1] is a *valid* index in Python)
    """
    possible_points = [ (row-1, col-1), (row-1, col), (row-1, col+1),
                        (row, col-1), (row, col+1),
                        (row+1, col-1), (row+1, col), (row+1, col+1)
                        ]
    
    adjacent_points = []

    for point in possible_points:
        if min(point) >= 0 and point[0] < num_rows and point[1] < num_cols:
            adjacent_points.append(point)
    
    return adjacent_points
