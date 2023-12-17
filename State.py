import random


class State:
    def __init__(self):
        self.puzzle = self.create_random_puzzle()

    def linear_search(self, target):
        """
        perform a linear search on the puzzle to find the target
        :param target: the value of the tile to look for
        :return: coordinates of the target tile
        """
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == target:
                    return [i, j]
        return [-1, -1]

    def create_random_puzzle(self):
        """
        create a random number list, shuffle it and
        use it to create a puzzle in form of a list of three lists of three numbers
        :return: a random puzzle
        """
        numbers = list(range(9))
        random.shuffle(numbers)
        self.empty_tile = [numbers.index(0) // 3, numbers.index(0) % 3]
        puzzle = [numbers[i * 3: i * 3 + 3] for i in range(3)]
        return puzzle

    def swap_tiles(self, first, second):
        """
        swap the tiles at the given coordinates and update the empty tile if it is one of the tiles being swapped
        :param first: first tile to swap
        :param second: second tile to swap
        """
        if self.puzzle[first[0]][first[1]] == 0:
            self.empty_tile = second
        elif self.puzzle[second[0]][second[1]] == 0:
            self.empty_tile = first
        self.puzzle[first[0]][first[1]], self.puzzle[second[0]][second[1]] = self.puzzle[second[0]][second[1]], \
                                                                             self.puzzle[first[0]][first[1]]

    def __str__(self):
        """
        returns the current state of the puzzle as a string
        :return:
        """
        return '\n'.join(' '.join(map(str, row)) for row in self.puzzle)

