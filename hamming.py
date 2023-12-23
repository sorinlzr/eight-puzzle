from PriorityQueueWithCounter import PriorityQueueWithCounter
from PuzzleNode import PuzzleNode, EMPTY_TILE_VALUE
from State import State
import copy

# Ausgangslage
initial_state = State()
puzzle = initial_state.puzzle

print("Initial state")
print(puzzle)
print()

algorithm = 'hamming'


# First "last_initial_tile_moved" is 0, so every direction would be possible in the first run.
initial_last_tile_moved = 0
initial_cost = 0
initial_node = PuzzleNode(initial_last_tile_moved, puzzle, initial_cost, algorithm)
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
    if node.heuristic <= 0:
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

                new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, algorithm)
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

                new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, algorithm)
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

                new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, algorithm)
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

                new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, algorithm)
                min_priority_queue.put(new_node, new_node.f_value)

print("Puzzle solved!")
print("Number of iterations " + str(number_of_iterations))
print("Initial Puzzle")
print(puzzle)
print("Final Puzzle")
print(finale_node.currentState)
print("Cost")
print(finale_node.cost)
