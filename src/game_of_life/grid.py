"""Module for defining grid classes.
"""

import copy

from game_of_life.node import Node


class Grid:
    """Main grid class."""

    def __init__(self, rows: int, cols: int, wrap: bool = False):
        self.rows = rows
        self.cols = cols
        self.mat = [[Node() for _ in range(cols)] for _ in range(rows)]
        self.wrap = wrap

    def __repr__(self):
        out = ""
        for row in self.mat:
            out += str([1 if x.alive else 0 for x in row]) + "\n"
        return out

    def num_neighbors(self, row: int, col: int):
        """Calculate number of living neighbors at the node.

        Args:
            row (int): row location of node to calculate at.
            col (int): column location of node to calculate at.

        Returns:
            int: Number of living neighbors at the node.
        """
        min_row = (row - 1) % self.rows
        max_row = (row + 1) % self.rows
        min_col = (col - 1) % self.cols
        max_col = (col + 1) % self.cols
        if not self.wrap:
            if (col - 1) < 0:
                min_col = 0
            if (col + 1) >= self.cols:
                max_col = self.cols - 1
            if (row - 1) < 0:
                min_row = 0
            if (row + 1) >= self.rows:
                max_row = self.rows - 1

        neighbors = 0
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                neighbors += 1 if self.mat[i][j].alive else 0
        neighbors -= 1 if self.mat[row][col].alive else 0
        return neighbors

    def step(self):
        """Perform a step of the game."""
        mat = copy.deepcopy(self.mat)
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.num_neighbors(i, j)
                if self.mat[i][j].alive:
                    if (neighbors <= 1) or (neighbors >= 4):
                        mat[i][j].flip()
                else:
                    if neighbors == 3:
                        mat[i][j].flip()
        self.mat = mat
        print(self)
