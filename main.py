"""
main.py - Submodule
- Inputs & Outputs :
    - Inputs :
        - Number of random puzzles to solve and create statistics from.

    - Outputs :
        - Information about Puzzles solved, including :
            - Initial Puzzle to be solved
            - Hamming - Execution Time
            - Hamming - Number of Nodes Expanded in Search Tree
            - Manhattan - Execution Time
            - Manhattan - Number of Nodes Expanded in Search Tree

- Function of the Submodule :
    The Main Class combines the functionality of all other modules.
    A custom number of randomly generated puzzles get solved by the Hamming and Manhattan algorithm, while tracking:
        - Hamming - Execution Time
        - Hamming - Number of Nodes Expanded in Search Tree
        - Manhattan - Execution Time
        - Manhattan - Number of Nodes Expanded in Search Tree
    Finally the "mean" and "standard deviation" of these values is calculated and printed.
"""

from PuzzleGenerator import PuzzleGenerator
from Algorithm import Algorithm
import time
import statistics

def main():
    # Create Empty Arrays
    hamming_execution_times = []
    manhattan_execution_times = []
    hamming_nodes_expanded = []
    manhattan_nodes_expanded = []

    print("Puzzle Nr ; Puzzle ; Algorithm ; Execution Time ; Number Of Nodes")

    for i in range(10):
        generator = PuzzleGenerator()
        puzzle = generator.create_random_puzzle()

        ############################################################################################################
        # Hamming Part
        ############################################################################################################

        hamming = Algorithm(puzzle, 'hamming')
        start_hamming = time.time()
        n_of_nodes_hamming = hamming.run()
        end_hamming = time.time()
        time_hamming = end_hamming - start_hamming

        hamming_execution_times.append(time_hamming)
        hamming_nodes_expanded.append(n_of_nodes_hamming)

        print("Puzzle " + str(i) + " ; " + str(puzzle) + " ; Hamming ; " + str(time_hamming) + " ; " + str(n_of_nodes_hamming))

        ############################################################################################################
        # Manhattan Part
        ############################################################################################################

        manhattan = Algorithm(puzzle, 'manhattan')
        start_manhattan = time.time()
        n_of_nodes_manhattan = manhattan.run()
        end_manhattan = time.time()
        time_manhattan = end_manhattan - start_manhattan

        manhattan_execution_times.append(time_manhattan)
        manhattan_nodes_expanded.append(n_of_nodes_manhattan)

        print("Puzzle " + str(i) + " ; " + str(puzzle) + " ; Manhattan ; " + str(time_manhattan) + " ; " + str(n_of_nodes_manhattan))

    print('###################################')
    print('Results:')
    print('Hamming - Execution Times[Seconds] - Mean: ' + str(statistics.mean(hamming_execution_times)))
    # "pstdev" <=> "Population Standard Deviation", because all values of the data set are used.
    print('Hamming - Execution Times[Seconds] - Standard Deviation: ' + str(statistics.pstdev(hamming_execution_times)))
    print('-')
    print('Manhattan - Execution Times[Seconds] - Mean: ' + str(statistics.mean(manhattan_execution_times)))
    # "pstdev" <=> "Population Standard Deviation", because all values of the data set are used.
    print('Manhattan - Execution Times[Seconds] - Standard Deviation: ' + str(statistics.pstdev(manhattan_execution_times)))
    print('-')
    print('Hamming - Expanded Nodes - Mean: ' + str(statistics.mean(hamming_nodes_expanded)))
    # "pstdev" <=> "Population Standard Deviation", because all values of the data set are used.
    print('Hamming - Expanded Nodes - Standard Deviation: ' + str(statistics.pstdev(hamming_nodes_expanded)))
    print('-')
    print('Manhattan - Expanded Nodes - Mean: ' + str(statistics.mean(manhattan_nodes_expanded)))
    # "pstdev" <=> "Population Standard Deviation", because all values of the data set are used.
    print('Manhattan - Expanded Nodes - Standard Deviation: ' + str(statistics.pstdev(manhattan_nodes_expanded)))

if __name__ == "__main__":
    main()
