import logging

from typing import Dict, Tuple

logger = logging.getLogger()


# Advent of Code Day 5 solution code


class Almanac:

    def __init__(self, text_input: str) -> None:
        str_sections = text_input.split("\n\n")
        
        # First line is the format "seeds: 1 2 3 4 5"
        seeds_str = str_sections[0].split(": ")[1]

        self.seeds = [int(seed) for seed in seeds_str.split()]

        # Everything else is a map
        self.maps = {}
        for map_str in str_sections[1:]:
            almanac_map = AlmanacMap(map_str)
            self.maps[almanac_map.source] = almanac_map
    
    def convert_seed_to_location(self, seed_no: int) -> int:
        category = "seed"
        source_no = seed_no
        log_str = f"Seed {seed_no}"

        while category != "location":
            category_map = self.maps[category]
            category, source_no = category_map.convert(source_no)
            log_str += f" -> {category} {source_no}"

        logger.info(log_str)

        return source_no
    
    def locate_all_seeds(self) -> Dict[int, int]:
        seed_locations = {seed: self.convert_seed_to_location(seed) for seed in self.seeds}

        return seed_locations


class AlmanacMap:

    def __init__(self, text_input: str) -> None:
        range_lines = text_input.split("\n")

        # First line is the format "source-to-destination map:"
        self.source, self.destination = range_lines[0].split()[0].split("-to-")

        self.ranges = []
        for range_line in range_lines[1:]:
            dest_start, source_start, range_len = range_line.split()
            self.ranges.append((int(dest_start), int(source_start), int(range_len)))

    def __repr__(self) -> str:
        return f"<{self.source}-to-{self.destination} map>"

    def convert(self, source_no: int) -> Tuple[str, int]:
        """Converts a number from the source to the destination.
        Returns the converted number and the destination type"""

        for dest_start, source_start, range_len in self.ranges:
            if source_no >= source_start and source_no <= (source_start + range_len - 1):
                range_offset = source_no - source_start
                destination_no = dest_start + range_offset
                return (self.destination, destination_no)

        # Any source numbers not mapped correspond to the same destination number
        return (self.destination, source_no)