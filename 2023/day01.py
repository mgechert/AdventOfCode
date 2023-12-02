from typing import List

# Advent of Code Day 1 solution code


DIGITS = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
WORD_SUBS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def calibrate_line(line: str) -> int:
    line_digits = [c for c in line if c in DIGITS]
    if len(line_digits) == 0:
        raise ValueError("Line contains no digits")

    value = int(line_digits[0] + line_digits[-1])

    return value

def calibrate_document(document: List[str]):
    calibration_total = 0

    for line in document:
        line_value = calibrate_line(line)
        calibration_total = calibration_total + line_value

    return calibration_total

# Part 2
def calibrate_line_v2(line: str) -> int:
    for word, sub in WORD_SUBS.items():
        line = line.replace(word, sub)

    return calibrate_line(line)

