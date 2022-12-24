from aoc_utils.PriorityQueue import PriorityQueue
from itertools import product
from typing import List, Tuple


def shortest_path(graph: List[List[Tuple[int, int]]]) -> int:
    pq = PriorityQueue()
    rows = len(graph)
    cols = len(graph[0])

    # Scan all points and load them into the priority queue, noting the Start
    for r, c in product(range(rows), range(cols)):
        pq.add(item=(r, c), priority=0 if graph[r][c] == 'S' else float('inf'))

    pass

    

def find_adjacent_nodes(graph: List[List[Tuple[int, int]]],
                        row: int, col: int) -> List[Tuple[int, int]]:
    """
    Checks the node in the graph at (row, col) and returns a list
    of all adjacent nodes that can be visited
    """
    elevations = 'SabcdefghijklmnopqrstuvwxyzE'
    this_node = graph[row][col]
    this_elevation = elevations.find(this_node)
    adjacent_nodes = []
   
    # These are the 8 (possibly) adjacent coordinates
    adjacent_coords = [
                       (row-1, col-1), (row-1, col), (row-1, col+1),
                       (row, col-1), (row, col+1),
                       (row+1, col-1), (row+1, col), (row+1, col+1)
                      ]

    # Check adjacent sets of coords and see if the node there is adjacent (if any)
    for adj_row, adj_col in adjacent_coords:
        if min(adj_row, adj_col) >= 0 and adj_row < len(graph) and adj_col < len(graph[0]):
            adjacent_node = graph[adj_row][adj_col]
            adjacent_elevation = elevations.find(adjacent_node)

            if adjacent_elevation - this_elevation < 2:
                adjacent_nodes.append((adj_row, adj_col))

    return adjacent_nodes
    