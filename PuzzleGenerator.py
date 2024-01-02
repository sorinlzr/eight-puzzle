"""
PuzzleGenerator.py - Submodule
- Inputs & Outputs :
    - Inputs :
        - Module has no inputs.

    - Outputs :
        - Random Puzzle which is guaranteed to be solvable.

- Function of the Submodule :
    The PuzzleGenerator Class generates a random puzzle, which got checked for solvability.
    The solvability is checked based upon the number of inversions, that occur within a puzzle.
        If the number of inversions is even, the puzzle can be solved.
        If the number is uneven, it can not be solved.
"""

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
        while True:
            numbers = list(range(9))
            random.shuffle(numbers)
            puzzle = [numbers[i * 3: i * 3 + 3] for i in range(3)]
            if self.is_solvable(numbers):
                return puzzle

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.puzzle)

