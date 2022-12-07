# Advent of Code Day 6 solution code

def find_marker(packet: str, marker_len: int) -> int:
    """
    Scans packet for the first consecutive sequence of distinct characters
    of length marker_len.
    Returns the index following the marker, or -1 if not found.
    """
    for i in range(marker_len, len(packet)):
        if len(set(packet[i-marker_len:i])) == marker_len:
            return i

    return -1


def find_packet_start(packet: str) -> int:
    """
    Finds the first occurence of the packet start marker, i.e. four distinct
    consecutive characters in the input string.
    """
    return find_marker(packet, marker_len=4)


def find_message_start(packet: str) -> int:
    """
    Finds the start of message, marker_length = 14
    """
    return find_marker(packet, marker_len=14)
