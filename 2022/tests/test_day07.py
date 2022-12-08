import pytest

from aoc_utils import parse_input_file
from day07 import FileSystem, build_fs_from_terminal


@pytest.fixture
def example_input():
    return parse_input_file("day07ex.txt")


@pytest.fixture
def fs():
    return FileSystem()


@pytest.fixture
def example_fs(example_input):
    return build_fs_from_terminal(example_input)


@pytest.fixture
def puzzle_fs():
    puzzle_input = parse_input_file("day07.txt")
    assert type(puzzle_input) is list
    assert len(puzzle_input) == 1022

    return build_fs_from_terminal(puzzle_input)


def test_example_input_correct_length(example_input):
    print(example_input)

    assert len(example_input) == 23


def test_fs_mkdir_updates_tree(fs):
    dir_name = 'test_dir'
    fs.mkdir(dir_name)

    print(fs.root)

    assert dir_name in fs.root


def test_fs_cd_changes_working_dir(fs):
    dir_name = 'test_dir'
    fs.mkdir(dir_name)
    fs.cd(dir_name)

    print(fs.root)

    assert fs.current_directory['.'] == dir_name


def test_fs_cd_change_to_parent_updates_working_dir(fs):
    dir_name = 'test_dir'
    fs.mkdir(dir_name)
    fs.cd(dir_name)
    fs.cd('..')

    print(fs.root)

    assert fs.current_directory['.'] == '/'


def test_fs_touch_creates_file_entry(fs):
    file_name = 'test_file'
    file_size = 1234
    fs.touch(file_name, file_size)

    assert file_name in fs.current_directory
    assert fs.current_directory[file_name] == file_size


def test_example_input_fs_contains_expected_objects(example_fs):
    print(example_fs.root)

    expected_root_objects = ['a', 'b.txt', 'c.dat', 'd']

    for expected in expected_root_objects:
        assert expected in example_fs.root


def test_get_catalog_calculates_expected_size(example_fs):
    catalog = example_fs.get_dir_catalog()

    expected = [('/', 48381165), ('a', 94853), ('e', 584), ('d', 24933642)]
    print(catalog)

    assert catalog == expected


def test_part1_example_solution(example_fs):
    """
    Part 1 solution: find all of the directories with a total size of at
    most 100000, then calculate the sum of their total sizes.
    """
    catalog = example_fs.get_dir_catalog()
    catalog = filter(lambda dir: dir[1] <= 100000, catalog)

    solution = sum([dir[1] for dir in catalog])

    assert solution == 95437


def test_part1_solution(puzzle_fs):
    """
    Part 1 solution: find all of the directories with a total size of at
    most 100000, then calculate the sum of their total sizes.
    """
    catalog = puzzle_fs.get_dir_catalog()
    catalog = filter(lambda dir: dir[1] <= 100000, catalog)

    solution = sum([dir[1] for dir in catalog])
    print(f"Part 1 solution is {solution}")

    # Accepted part 1 solution
    assert solution == 1141028


# Part 2
def test_part2_example_solution(example_fs):
    """
    Find the smallest directory that, if deleted, would free up enough space
    on the filesystem to run the update. What is the total size of that
    directory?
    """
    total_space = 70000000
    required_free = 30000000
    catalog = example_fs.get_dir_catalog()
    total_used = catalog[0][1]  # catalog[0] is the item for the root folder
    current_unused = total_space - total_used
    min_to_delete = required_free - current_unused

    # These are the dirs big enough to clear the minimum space
    catalog = filter(lambda dir: dir[1] >= min_to_delete, catalog)
    delete_dir = sorted(catalog, key=lambda dir: dir[1])[0]
    delete_size = delete_dir[1]

    print(f"Delete dir is {delete_dir}")

    assert delete_size == 24933642


def test_part2_solution(puzzle_fs):
    """
    Find the smallest directory that, if deleted, would free up enough space
    on the filesystem to run the update. What is the total size of that
    directory?
    """
    total_space = 70000000
    required_free = 30000000
    catalog = puzzle_fs.get_dir_catalog()
    total_used = catalog[0][1]  # catalog[0] is the item for the root folder
    current_unused = total_space - total_used
    min_to_delete = required_free - current_unused

    # These are the dirs big enough to clear the minimum space
    catalog = filter(lambda dir: dir[1] >= min_to_delete, catalog)
    delete_dir = sorted(catalog, key=lambda dir: dir[1])[0]
    delete_size = delete_dir[1]

    print(f"Part 2 solution is {delete_size}")

    # Accepted part 2 solution
    assert delete_size == 8278005
