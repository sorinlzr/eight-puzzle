import random


class PuzzleGenerator:
    def __init__(self):
        self.puzzle = self.create_random_puzzle()

    def get_inv_count(self, arr):
        inv_count = 0
        for i in range(8):
            for j in range(i + 1, 9):
                if arr[j] and arr[i] and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    def is_solvable(self, numbers):
        inv_count = self.get_inv_count(numbers)
        return inv_count % 2 == 0

    def create_random_puzzle(self):
        """
        Create a random number list, shuffle it and
        use it to create a puzzle in form of a list of three lists of three numbers.
        It also checks the solvability of the puzzle, if a number of inversions are even in the input state.
        A pair of tiles form an inversion if the values on tiles are in reverse order of their appearance in goal state
        :return: a random puzzle
        """
        while True:
            numbers = list(range(9))
            random.shuffle(numbers)
            puzzle = [numbers[i * 3: i * 3 + 3] for i in range(3)]
            if self.is_solvable(numbers):
                return puzzle

    def __str__(self):
        """
        returns the current state of the puzzle as a string
        :return:
        """
        return '\n'.join(' '.join(map(str, row)) for row in self.puzzle)
