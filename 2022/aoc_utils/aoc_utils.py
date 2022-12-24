import os
from typing import Callable


def parse_input_file(filename: str,
                     parse_line: Callable = lambda line: line.strip(),
                     inputs_path: str = None) -> list:
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
