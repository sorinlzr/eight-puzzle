MAX_TILES_HORIZONTAL = 3
MAX_TILES_VERTICAL = 3
EMPTY_TILE_VALUE = 0


def calculate_distance_from_destination(current_x_coord, current_y_coord, affected_tile):
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


class PuzzleNode:
    def __init__(self, last_moved_tile, current_state, cost, algorithm):
        self.last_moved_tile = last_moved_tile
        self.currentState = current_state
        self.cost = cost
        self.heuristic = 0
        self.f_value = 0
        self.algorithm = algorithm
        self._calc_heuristic_and_f_value()

    def __repr__(self):
        return f"PuzzleNode(last_moved_tile={self.last_moved_tile}, currentState={self.currentState}, cost={self.cost}, heuristic={self.heuristic}, f_value={self.f_value})"

    # Nur in Konstruktor aufrufen
    def _calc_heuristic_and_f_value(self):
        if self.algorithm == 'hamming':
            for i in range(MAX_TILES_VERTICAL):
                for j in range(MAX_TILES_HORIZONTAL):
                    if self.currentState[i][j] != (i * 3 + j):
                        self.heuristic += 1
            # Since 0 implies the empty value, and never gets a match
            # the heuristic gets decreased by 1
            self.heuristic -= 1
            # F-Value gets calculated.
            self.f_value = self.cost + self.heuristic
        elif self.algorithm == 'manhattan':
            for i in range(MAX_TILES_VERTICAL):
                for j in range(MAX_TILES_HORIZONTAL):
                    if self.currentState[i][j] != EMPTY_TILE_VALUE:
                        self.heuristic += calculate_distance_from_destination(j, i, self.currentState[i][j])

            # F-Value gets calculated.
            self.f_value = self.cost + self.heuristic

    def get_coordinates_of_empty_tile(self):
        for i in range(MAX_TILES_VERTICAL):
            for j in range(MAX_TILES_HORIZONTAL):
                if self.currentState[i][j] == EMPTY_TILE_VALUE:
                    return i, j