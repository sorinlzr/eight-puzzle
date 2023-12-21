from queue import PriorityQueue
import copy

# Ausgangslage
EMPTY_TILE_VALUE = -1
initial_state = [[7, 2, 4], [5, EMPTY_TILE_VALUE, 6], [8, 3, 1]]
MAX_TILES_HORIZONTAL = len(initial_state)
MAX_TILES_VERTICAL = len(initial_state[0])


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


class puzzleNode:
    def __init__(self, last_moved_tile, current_state, cost):
        self.last_moved_tile = last_moved_tile
        self.currentState = current_state
        self.cost = cost
        self.heuristic = 0
        self.f_value = 0
        self._calc_heuristic_and_f_value()

    def __repr__(self):
        return f"PuzzleNode(last_moved_tile={self.last_moved_tile}, currentState={self.currentState}, cost={self.cost}, heuristic={self.heuristic}, f_value={self.f_value})"

    # Nur in Konstruktor aufrufen
    def _calc_heuristic_and_f_value(self):
        i = 0
        while i < MAX_TILES_VERTICAL:
            j = 0
            while j < MAX_TILES_HORIZONTAL:
                if self.currentState[i][j] != EMPTY_TILE_VALUE:
                    self.heuristic += calculate_distance_from_destination(j, i,self.currentState[i][j])
                j += 1
            i += 1

        # F-Value gets calculated.
        self.f_value = self.cost + self.heuristic

    def get_coordinates_of_empty_tile(self):
        i = 0
        while i < MAX_TILES_VERTICAL:
            j = 0
            while j < MAX_TILES_HORIZONTAL:
                if self.currentState[i][j] == EMPTY_TILE_VALUE:
                    return (i, j)
                    # print(currentState[i][j], end=' ')
                j += 1
            # print()  # Move to the next line after each row
            i += 1

# Allgemeine Funktion
def calculate_distance_from_destination(current_x_coord,current_y_coord, affected_tile):
    total_tile_distance = 0
    # define destination row of affected_tile
    destination_row = affected_tile // 3
    # define destination column of affected_tile
    destination_column = affected_tile % 3

    if destination_row >= current_y_coord:
        total_tile_distance += destination_row - current_y_coord
    else:
        total_tile_distance += current_y_coord - destination_row

    if destination_column >= current_x_coord:
        total_tile_distance += destination_column - current_x_coord
    else:
        total_tile_distance += current_x_coord - destination_column

    return total_tile_distance


# First "last_initial_tile_moved" is 0, so every direction would be possible in the first run.
initial_last_tile_moved = 0
initial_cost = 0
initial_node = puzzleNode(initial_last_tile_moved, initial_state, initial_cost)
finale_node = None
# print(initial_node)

# Example usage:
min_priority_queue = PriorityQueueWithCounter()
min_priority_queue.put(initial_node, initial_node.f_value)

solution_found = False
number_of_iterations = 0
while not solution_found:  # min_priority_queue.is_empty():
    node = min_priority_queue.get()

    # Hier wird überprüft, ob das Puzzle gelöst wurde.
    if node.heuristic == 0:
        solution_found = True
        finale_node = node
    else:
        number_of_iterations += 1
        # Koordinaten von Empty Tile suchen
        coordinates = node.get_coordinates_of_empty_tile()
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]

        # Wäre tauschen nach oben möglich?
        if y_coordinate >= 1:
            new_y_coordinate = y_coordinate - 1
            if node.currentState[x_coordinate][new_y_coordinate] != node.last_moved_tile:
                new_last_tile_moved = node.currentState[x_coordinate][new_y_coordinate]

                # Sorgt für ein Duplikat des gesamten 2D-Arrays.
                new_state = copy.deepcopy(node.currentState)
                new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                new_state[x_coordinate][new_y_coordinate] = EMPTY_TILE_VALUE

                new_cost = node.cost + 1

                new_node = puzzleNode(new_last_tile_moved, new_state, new_cost)
                min_priority_queue.put(new_node, new_node.f_value)

        # Teste tauschen nach rechts
        if x_coordinate <= 1:
            new_x_coordinate = x_coordinate + 1
            if node.currentState[new_x_coordinate][y_coordinate] != node.last_moved_tile:
                new_last_tile_moved = node.currentState[new_x_coordinate][y_coordinate]

                # Sorgt für ein Duplikat des gesamten 2D-Arrays.
                new_state = copy.deepcopy(node.currentState)
                new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                new_state[new_x_coordinate][y_coordinate] = EMPTY_TILE_VALUE

                new_cost = node.cost + 1

                new_node = puzzleNode(new_last_tile_moved, new_state, new_cost)
                min_priority_queue.put(new_node, new_node.f_value)

        # Teste tauschen nach unten
        if y_coordinate <= 1:
            new_y_coordinate = y_coordinate + 1
            if node.currentState[x_coordinate][new_y_coordinate] != node.last_moved_tile:
                new_last_tile_moved = node.currentState[x_coordinate][new_y_coordinate]

                # Sorgt für ein Duplikat des gesamten 2D-Arrays.
                new_state = copy.deepcopy(node.currentState)
                new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                new_state[x_coordinate][new_y_coordinate] = EMPTY_TILE_VALUE

                new_cost = node.cost + 1

                new_node = puzzleNode(new_last_tile_moved, new_state, new_cost)
                min_priority_queue.put(new_node, new_node.f_value)

        # Teste tauschen nach links
        if x_coordinate >= 1:
            new_x_coordinate = x_coordinate - 1
            if node.currentState[new_x_coordinate][y_coordinate] != node.last_moved_tile:
                new_last_tile_moved = node.currentState[new_x_coordinate][y_coordinate]

                # Sorgt für ein Duplikat des gesamten 2D-Arrays.
                new_state = copy.deepcopy(node.currentState)
                new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                new_state[new_x_coordinate][y_coordinate] = EMPTY_TILE_VALUE

                new_cost = node.cost + 1

                new_node = puzzleNode(new_last_tile_moved, new_state, new_cost)
                min_priority_queue.put(new_node, new_node.f_value)

print("Puzzle solved!")
print("Number of iterations " + str(number_of_iterations))
print("Initial Puzzle")
print(initial_state)
print("Final Puzzle")
print(finale_node.currentState)
print("Heuristic")
print(finale_node.heuristic)
print("Cost")
print(finale_node.cost)
