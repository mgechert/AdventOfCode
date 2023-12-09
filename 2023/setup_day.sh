#!/bin/bash
echo "Setting up files for day $1"
filename_base=`printf day%02d $1`
solution_file="$filename_base.py"
tests_file="./tests/test_$filename_base.py"
input_ex_file="./tests/inputs/${filename_base}ex.txt"
input_file="./tests/inputs/${filename_base}.txt"

if test -e "$solution_file"; then
	echo "$solution_file already exists, aborting"
	exit 1
fi

echo "Creating $solution_file"
cat <<EOF >> $solution_file
import logging

logger = logging.getLogger()


# Advent of Code Day $1 solution code


EOF

echo "Creating tests file $tests_file"
cat <<EOF >> $tests_file
import pytest

from aoc_utils import parse_input_file

@pytest.fixture
def ex1_input():
    return parse_input_file("${filename_base}ex.txt")


@pytest.fixture
def problem_input():
    return parse_input_file("${filename_base}.txt")

def test_read_inputs(ex1_input, problem_input):
    # Sanity check - did the inputs get completely read?
    ex_len = len(ex1_input)
    in_len = len(problem_input)

    expected_ex_len = 0
    expected_in_len = 0

    assert ex_len == expected_ex_len
    assert in_len == expected_in_len

EOF


echo "Creating empty inputs files $input_ex_file, $input_file"
touch $input_ex_file
touch $input_file
