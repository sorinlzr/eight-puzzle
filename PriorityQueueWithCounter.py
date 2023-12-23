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