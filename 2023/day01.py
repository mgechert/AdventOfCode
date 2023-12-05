from typing import List, Tuple
# from typing_extensions import Self

# Advent of Code Day 1 solution code


DIGITS = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
WORDS_DIGITS = {
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


def calibrate_document(document: List[str]) -> int:
    calibration_total = 0

    for line in document:
        line_value = calibrate_line(line)
        calibration_total = calibration_total + line_value

    return calibration_total

# Part 2


class Trie:

    class Node:
        def __init__(self) -> None:
            self.children = {}
            self.matching_word = None

        def get_child(self, key: str):
            if key not in self.children:
                self.children[key] = self.__class__()

            return self.children[key]

    def __init__(self) -> None:
        self.root = self.Node()

    def insert(self, word: str) -> None:
        """Insert a word to the trie"""
        if len(word) == 0:
            return

        self._insert(self.root, word, 0)

    def _insert(self, node: Node, word: str, index: int) -> None:
        """Recursive insert"""
        child = node.get_child(word[index])

        if index == len(word) - 1:
            child.matching_word = word
        else:
            self._insert(child, word, index + 1)

    def print(self) -> None:
        self._print(self.root)

    def _print(self, node: Node, prefix="") -> None:
        """Recursive print"""
        if node.matching_word:
            print(f"******WORD: {node.matching_word}")

        for key, child_node in node.children.items():
            display_str = prefix + key + "-"
            print(display_str)
            self._print(child_node, display_str)

    def search(self, search_string: str) -> Tuple[str, str]:
        """Scans the search string recursively for a match"""
        return self._search(self.root, search_string, 0)

    def _search(self, node: Node, search_string: str, index: int) -> str:
        """Recursive search"""
        if index < len(search_string) and search_string[index] in node.children:
            child_node = node.children[search_string[index]]
            child_result = self._search(child_node, search_string, index + 1)
            # Return the child result if there is one, otherwise this node (may be None)
            return child_result or node.matching_word
        else:
            return node.matching_word

    def find_all(self, search_string: str) -> List[str]:
        """Find all matches inside search_string"""
        results = []
        i = 0

        while i < len(search_string):
            result = self.search(search_string[i:])
            if result:
                results.append(result)
            i = i + 1

        return results


def scan_document(document: List[str]) -> List[int]:
    """Scans every line in the list and returns the
    int result of the first and last digits found in each line"""
    trie = Trie()
    results = []

    for word, digit in WORDS_DIGITS.items():
        trie.insert(word)
        trie.insert(digit)

    for line in document:
        line_results = trie.find_all(line)
        left, right = line_results[0], line_results[-1]

        # Replace words with digits where applicable
        left = WORDS_DIGITS.get(left, left)
        right = WORDS_DIGITS.get(right, right)

        int_result = int(left + right)
        results.append(int_result)

    return results
