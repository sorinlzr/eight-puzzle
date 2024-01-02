"""
PriorityQueueWithCounter.py - Submodule
- Inputs & Outputs :
    - Inputs :
        - Allows to put new items in to the Priority Queue.

    - Outputs :
        - Allows to get the highest priority item from the queue.
        - Allows to check, whether the Queue is empty

- Function of the Submodule :
    The PriorityQueue Class stores PuzzleNodes.
    The Priority Queue has an entry counter :
        - Reason :
            If two elements are put into the Queue with the same priority, the value of the item is used to
            determine the position within the Queue. In this case the values are Objects of the Class "PuzzleNode"
            and are therefore not comparable.
        - The entry counter is a comparable number which is used to put prioritize multiple items with the same priority
"""

from queue import PriorityQueue


class PriorityQueueWithCounter:
    def __init__(self):
        self.pq = PriorityQueue()
        self.entry_counter = 0

    def put(self, item, priority):
        # entry_counter serves to order items with the same priority
        # (also ensures that two items with the same priority won't attempt to sort by comparing the values)
        entry = [priority, self.entry_counter, item]
        self.pq.put(entry)
        self.entry_counter += 1

    def get(self):
        return self.pq.get()[-1]

    def empty(self):
        return self.pq.empty()
