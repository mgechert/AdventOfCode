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
echo "# Advent of Code Day $1 solution code" >> $solution_file


echo "Creating tests file $tests_file"
test_header="import pytest
from $filename_base import *"

echo $test_header >> $tests_file


echo "Creating empty inputs files $input_ex_file, $input_file"
touch $input_ex_file
touch $input_file
