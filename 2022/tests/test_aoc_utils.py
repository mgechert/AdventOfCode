from aoc_utils import parse_input_file


def test_parse_input_file_reads_plain_file():
    """
    With no parser supplied, parse_input_file() should just return
    a list of strings, one per line with str.strip() applied to each
    """
    input = parse_input_file("day03ex.txt")

    print(input[0])

    assert type(input) is list
    assert len(input) == 6
    assert input[0] == "vJrwpWtwJgWrhcsFMMfFFhFp"


def test_parse_with_parser_reads_input_file():
    """
    With a custom parser parse_input_file() will return a list of
    arbitrary object(s), eg tuples of strings, ints, etc.
    """
    def parser(line: str):
        # Return a tuple of the first 3 chars and the line length
        return (line[:3], len(line.strip()))

    input = parse_input_file("day03ex.txt", parser)

    assert type(input) is list
    assert len(input) == 6
    assert input[0] == ("vJr", 24)
