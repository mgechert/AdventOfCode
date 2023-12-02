from heapq import heappush, heappop
import itertools


class PriorityQueue:
    """
    Generalized priority queue originally from AOC 2021 day 15
    see also https://docs.python.org/3/library/heapq.html
    """
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def add(self, item, priority=float("inf")):
        """Add a item to the queue (remove/replace if it is already there)"""
        if item in self.entry_finder:
            self.remove_item(item)
        count = next(self.counter)
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heappush(self.pq, entry)

    def remove_item(self, item):
        """
        Mark a queue entry as removed by removing it from the entry_finder
        and setting the item to None in the pq
        """
        entry = self.entry_finder.pop(item)
        entry[-1] = None  # entry is a ref to a list: this updates item in the pq

    def pop(self):
        """
        Remove entries from the queue until one references a item,
        returns tuple of (item, priority)
        """
        while self.pq:
            priority, _, item = heappop(self.pq)
            if item is not None:
                del (self.entry_finder[item])
                return (item, priority)
        raise KeyError("Can not pop when queue is empty")

    def update(self, item, priority):
        """
        If specified priority is _higher_ than the item's current priority, no
            changes are made.
        If item exists in the queue and the specified priority is _lower_ than
            its current priority, update the item's queue priority to the lower
            priority.
        If item is not in queue, add it with the specified priority.
        """
        if (self.contains(item) and priority < self[item]) or not self.contains(item):
            self.add(item, priority)

    def contains(self, item):
        return item in self.entry_finder

    def __getitem__(self, item):
        """Return the priority of item"""
        return self.entry_finder[item][0]

    def __setitem__(self, item, priority):
        """Update the item priority only if it already exists"""
        if item in self.entry_finder:
            self.add_item(item, priority=priority)
        else:
            raise KeyError

    def __len__(self):
        # Length of the queue is the number of items, not the pq length
        return len(self.entry_finder)
