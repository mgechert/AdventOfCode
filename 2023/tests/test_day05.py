import pytest

from aoc_utils import read_raw_input_file
from day05 import Almanac

@pytest.fixture
def ex1_input():
    return read_raw_input_file("day05ex.txt")


@pytest.fixture
def problem_input():
    return read_raw_input_file("day05.txt")

def test_read_inputs(ex1_input, problem_input):
    # Sanity check - did the inputs get completely read?
    ex_start, ex_end = ex1_input[:5], ex1_input[-5:]
    in_start, in_end = problem_input[:5], problem_input[-5:]

    expected_ex_start, expected_ex_end = "seeds", " 93 4"
    expected_in_start, expected_in_end = "seeds", "23942"

    assert (ex_start, ex_end) == (expected_ex_start, expected_ex_end)
    assert (in_start, in_end) == (expected_in_start, expected_in_end)


def test_almanac_reads_expected_seeds(ex1_input):
    almanac = Almanac(ex1_input)
    
    expected_seeds = [79, 14, 55, 13]
    
    assert almanac.seeds == expected_seeds


def test_almanac_reads_expected_maps(ex1_input):
    almanac = Almanac(ex1_input)
    num_maps = len(almanac.maps)

    num_expected_maps = 7
    print(almanac.maps)

    assert num_maps == num_expected_maps


def test_almanac_map_reads_expected_map_ranges(ex1_input):
    almanac = Almanac(ex1_input)
    seed_soil_map = almanac.maps["seed"]
    num_ranges = len(seed_soil_map.ranges)

    expected_num_ranges = 2
    expected_ranges = [(50, 98, 2), (52, 50, 48)]
    print(seed_soil_map.ranges)

    assert num_ranges == expected_num_ranges
    assert seed_soil_map.ranges == expected_ranges


def test_almanac_map_converts_seed_to_soil(ex1_input):
    almanac = Almanac(ex1_input)
    seed_soil_map = almanac.maps["seed"]

    soil_type, soil_no = seed_soil_map.convert(98)

    expected_type = "soil"
    expected_no = 50

    assert soil_type == expected_type
    assert soil_no == expected_no


def test_almanac_map_converts_unmapped_seed_to_soil(ex1_input):
    almanac = Almanac(ex1_input)
    seed_soil_map = almanac.maps["seed"]

    soil_type, soil_no = seed_soil_map.convert(10)

    expected_type = "soil"
    expected_no = 10

    assert soil_type == expected_type
    assert soil_no == expected_no


def test_almanac_map_converts_seed_to_location(ex1_input):
    almanac = Almanac(ex1_input)
    location = almanac.convert_seed_to_location(79)

    expected_location = 82

    assert location == expected_location


def test_example1(ex1_input):
    almanac = Almanac(ex1_input)
    locations = almanac.locate_all_seeds()

    expected_locations = [82, 43, 86, 35]
    expected_min = 35
    print(locations)

    assert list(locations.values()) == expected_locations
    assert min(locations.values()) == expected_min


def test_part1_solution(problem_input):
    almanac = Almanac(problem_input)
    locations = almanac.locate_all_seeds()
    solution = min(locations.values())

    accepted_solution = 324724204
    print(f"Part 1 solution: {solution}")

    assert solution == accepted_solution
