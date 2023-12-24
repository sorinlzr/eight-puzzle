from PuzzleGenerator import PuzzleGenerator
from Algorithm import Algorithm
import time
import statistics

def main():
    hamming_execution_times = []
    manhattan_execution_times = []
    hamming_nodes_expanded = []
    manhattan_nodes_expanded = []

    for i in range(100):
        generator = PuzzleGenerator()
        puzzle = generator.create_random_puzzle()

        print()
        print()
        print("Initial state of Puzzle Number: " + str(i))
        print(puzzle)

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

        #print('Hamming - Execution time in seconds: ' + str(time_hamming))
        #print('Hamming - Number of entries in priority queue: ' + str(n_of_nodes_hamming))

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

        #print('Hamming - Execution time in seconds: ' + str(time_manhattan))
        #print('Manhattan - Number of entries in priority queue: ' + str(n_of_nodes_manhattan))

    print('###################################')
    print('Results:')
    print('Hamming - Execution Times[Seconds] - Mean: ' + str(statistics.mean(hamming_execution_times)))
    print('Hamming - Execution Times[Seconds] - Standard Deviation: ' + str(statistics.stdev(hamming_execution_times)))
    print('-')
    print('Manhattan - Execution Times[Seconds] - Mean: ' + str(statistics.mean(manhattan_execution_times)))
    print('Manhattan - Execution Times[Seconds] - Standard Deviation: ' + str(statistics.stdev(manhattan_execution_times)))
    print('-')
    print('Hamming - Expanded Nodes - Mean: ' + str(statistics.mean(hamming_nodes_expanded)))
    print('Hamming - Expanded Nodes - Standard Deviation: ' + str(statistics.stdev(hamming_nodes_expanded)))
    print('-')
    print('Manhattan - Expanded Nodes - Mean: ' + str(statistics.mean(manhattan_nodes_expanded)))
    print('Manhattan - Expanded Nodes - Standard Deviation: ' + str(statistics.stdev(manhattan_nodes_expanded)))

if __name__ == "__main__":
    main()
