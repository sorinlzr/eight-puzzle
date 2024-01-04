"""
Algorithm.py - Submodule
- Inputs & Outputs :
    - Inputs :
        - Initial Puzzle.
        - Algorithm to use for solving the puzzle.

    - Outputs :
        - The Number of Nodes that were added to the PriorityQueue in total.

- Function of the Submodule :
    The Algorithm Class solves the puzzle.
    - Initially there is a PuzzleNode Created, which is put into the PriorityQueue.
    - An endless loop always gets the highest priority PuzzleNode out of the Queue and checks possible tile movements.
        - When a tile movement would revert the previous swap, the move is ignored.
        - The loop runs, until the solved puzzled is pulled out of the priority queue.
"""

from PuzzleNode import PuzzleNode, EMPTY_TILE_VALUE
from PriorityQueueWithCounter import PriorityQueueWithCounter
import copy

class Algorithm:
    def __init__(self, puzzle, algorithm):
        self.puzzle = puzzle
        self.algorithm = algorithm

    def run(self):
        # First "last_initial_tile_moved" is 0, so every direction would be possible in the first run.
        initial_last_tile_moved = 0
        initial_cost = 0
        initial_node = PuzzleNode(initial_last_tile_moved, self.puzzle, initial_cost, self.algorithm)


        min_priority_queue = PriorityQueueWithCounter()
        min_priority_queue.put(initial_node, initial_node.f_value)

        number_of_iterations = 0
        while True:
            node = min_priority_queue.get()

            # Check if puzzle got solved.
            if node.heuristic == 0:
                return min_priority_queue.entry_counter
            else:
                number_of_iterations += 1
                coordinates = node.get_coordinates_of_empty_tile()
                x_coordinate = coordinates[0]
                y_coordinate = coordinates[1]

                # Would a swap with an above tile be possible?
                if y_coordinate >= 1:
                    new_y_coordinate = y_coordinate - 1
                    # Would this swap revert the previous swap?
                    if node.currentState[x_coordinate][new_y_coordinate] != node.last_moved_tile:
                        new_last_tile_moved = node.currentState[x_coordinate][new_y_coordinate]

                        # Creates a duplicate of the whole 2D-Array - including subarrays.
                        new_state = copy.deepcopy(node.currentState)

                        # Swapping Tiles
                        new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                        new_state[x_coordinate][new_y_coordinate] = EMPTY_TILE_VALUE

                        new_cost = node.cost + 1

                        # Create New PuzzleNode and store it in PriorityQueue
                        new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, self.algorithm)
                        min_priority_queue.put(new_node, new_node.f_value)

                # Would a swap with a tile to the right be possible?
                if x_coordinate <= 1:
                    new_x_coordinate = x_coordinate + 1
                    # Would this swap revert the previous swap?
                    if node.currentState[new_x_coordinate][y_coordinate] != node.last_moved_tile:
                        new_last_tile_moved = node.currentState[new_x_coordinate][y_coordinate]

                        # Creates a duplicate of the whole 2D-Array - including subarrays.
                        new_state = copy.deepcopy(node.currentState)

                        # Swapping Tiles
                        new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                        new_state[new_x_coordinate][y_coordinate] = EMPTY_TILE_VALUE

                        new_cost = node.cost + 1

                        # Create New PuzzleNode and store it in PriorityQueue
                        new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, self.algorithm)
                        min_priority_queue.put(new_node, new_node.f_value)

                # Would a swap with a below tile be possible?
                if y_coordinate <= 1:
                    new_y_coordinate = y_coordinate + 1
                    # Would this swap revert the previous swap?
                    if node.currentState[x_coordinate][new_y_coordinate] != node.last_moved_tile:
                        new_last_tile_moved = node.currentState[x_coordinate][new_y_coordinate]

                        # Creates a duplicate of the whole 2D-Array - including subarrays.
                        new_state = copy.deepcopy(node.currentState)

                        # Swapping Tiles
                        new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                        new_state[x_coordinate][new_y_coordinate] = EMPTY_TILE_VALUE

                        new_cost = node.cost + 1

                        # Create New PuzzleNode and store it in PriorityQueue
                        new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, self.algorithm)
                        min_priority_queue.put(new_node, new_node.f_value)

                # Would a swap with a tile to the right be possible?
                if x_coordinate >= 1:
                    new_x_coordinate = x_coordinate - 1
                    # Would this swap revert the previous swap?
                    if node.currentState[new_x_coordinate][y_coordinate] != node.last_moved_tile:
                        new_last_tile_moved = node.currentState[new_x_coordinate][y_coordinate]

                        # Creates a duplicate of the whole 2D-Array - including subarrays.
                        new_state = copy.deepcopy(node.currentState)

                        # Swapping Tiles
                        new_state[x_coordinate][y_coordinate] = new_last_tile_moved
                        new_state[new_x_coordinate][y_coordinate] = EMPTY_TILE_VALUE

                        new_cost = node.cost + 1

                        # Create New PuzzleNode and store it in PriorityQueue
                        new_node = PuzzleNode(new_last_tile_moved, new_state, new_cost, self.algorithm)
                        min_priority_queue.put(new_node, new_node.f_value)
