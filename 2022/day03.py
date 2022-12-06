from typing import List

PRIORITY = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def calculate_rucksack_priority(items: str) -> int:
    """
    Identify the item(s) appearing in both compartments and return the
    total priority.
    """
    mid = len(items) // 2
    shared_items = set(items[:mid]).intersection(set(items[mid:]))
    priority = 0

    for shared_item in shared_items:
        priority = priority + PRIORITY.find(shared_item)

    return priority


def calculate_group_priority(group_rucksacks: List[str]) -> int:
    """
    Identify the single item appearing in all of the group's rucksacks and
    return its priority
    """
    if len(group_rucksacks) != 3:
        raise ValueError('Must pass exactly 3 rucksacks')

    group_badge = set(group_rucksacks[0])\
        .intersection(set(group_rucksacks[1]))\
        .intersection(set(group_rucksacks[2]))

    if len(group_badge) != 1:
        raise ValueError('Rucksacks must contain exactly 1 item in common')

    item = group_badge.pop()

    return PRIORITY.find(item)
