import logging

from math import floor
from typing import List, Tuple

logger = logging.getLogger()

# Advent of Code Day 4 solution code

class CardScanner:
    def __init__(self, card_strs: List[str]) -> None:
        self.cards = [self.parse_card_str(card_str) for card_str in card_strs]
        self.total_scratchcards = 0

    @classmethod
    def parse_card_str(cls, card_str: str) -> Tuple[int, List[int], List[int]]:
        card_no_str, card_nums_str = card_str.split(":")
        _, card_no = card_no_str.split()
        winning_nums_str, drawn_nums_str = card_nums_str.split("|")
        winning_nums = winning_nums_str.split()
        drawn_nums = drawn_nums_str.split()
        card_score, winning_num_count = cls.calculate_card_score(winning_nums, drawn_nums)

        return (int(card_no), card_score, winning_nums, drawn_nums, winning_num_count)

    @classmethod
    def calculate_card_score(cls, winning_nums: List[str], drawn_nums: List[str]) -> Tuple[int]:
        winning_num_count = len(set(winning_nums).intersection(set(drawn_nums)))
        card_score = floor(2**(winning_num_count - 1))

        return (card_score, winning_num_count)
    
    def calculate_total_cards(self):
        """Part 2 solution"""
        card_counts = [1] * len(self.cards)

        for i, card in enumerate(self.cards):
            this_card_qty = card_counts[i]
            winning_num_count = card[4]

            for j in range(i + 1, i + 1 + winning_num_count):
                card_counts[j] = card_counts[j] + this_card_qty

        logger.info(f"Scratchcard Counts: {card_counts}")

        return sum(card_counts)








