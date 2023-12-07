from typing import Tuple

# Advent of Code Day 2 solution code


def is_game_possible(game: dict, constraint: Tuple[int, int, int]) -> bool:
    """Checks if game is possible given constraint of number of cubes
    constraint is a tuple of (red, green, blue)
    """
    max_r, max_g, max_b = constraint

    for result in game["game_results"]:
        if (result["red"] > max_r
            or result["green"] > max_g
            or result["blue"] > max_b):

            return False
    
    return True


def fewest_cubes_possible(game: dict) -> Tuple[int, int, int]:
    reds = [result["red"] for result in game["game_results"]]
    greens = [result["green"] for result in game["game_results"]]
    blues = [result["blue"] for result in game["game_results"]]

    fewest_cubes = (max(reds), max(greens), max(blues))

    return fewest_cubes
