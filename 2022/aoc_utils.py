import os
from typing import List

INPUTS_PATH = os.path.join(os.path.dirname(__file__), "tests/inputs")


def input_file_to_str_list(filename: str) -> List[str]:
    output = []
    with open(f"{INPUTS_PATH}/{filename}") as f:
        for line in f.readlines():
            output.append(line.strip())
    
    return output
