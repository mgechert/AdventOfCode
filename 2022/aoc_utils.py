import os
from typing import Callable

INPUTS_PATH = os.path.join(os.path.dirname(__file__), "tests/inputs")


def parse_input_file(filename: str,
                     parse_line: Callable = lambda line: line.strip()) -> list:
    """
    Read the given input file into a list, applying the optional
    parse_fn
    """
    output = []

    with open(f"{INPUTS_PATH}/{filename}") as f:
        for line in f.readlines():
            output.append(parse_line(line))

    return output
