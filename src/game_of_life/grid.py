"""Module for defining grid classes.
"""

from typing import Callable

from game_of_life.node import Node


class Grid:
    """Main grid class."""

    def __init__(self, rows: int, cols: int, wrap: bool = False):
        self.rows = rows
        self.cols = cols
        self.wrap = wrap
        self.mat = self.initialize_grid()
        self.update_list: set[tuple[int, int]] = set()
        self.future_update_list: set[tuple[int, int]] = set()
        self.flip_queue: list[Callable] = []

    def __repr__(self):
        out = ""
        for row in self.mat:
            out += str([1 if x.alive else 0 for x in row]) + "\n"
        return out

    def initialize_nodes(self, coord_list: list[tuple[int, int]]):
        """initialize nodes"""
        for row, col in coord_list:
            self.flip_node(row, col)
        self.execute_flips()

    def flip_node(self, row: int, col: int):
        """flip the node and adds all its neighbors to the update list"""
        node = self.mat[row][col]
        self.flip_queue.append(node.flip)
        self.future_update_list = self.future_update_list.union(node.neighbors)

    def initialize_grid(self):
        """initialize grid"""
        mat = [[Node(row, col) for col in range(self.cols)] for row in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                mat[row][col].neighbors = mat[row][col].neighbors.union(
                    self.get_neighbors(row, col)
                )
        return mat

    def get_neighbors(self, row: int, col: int) -> set[tuple[int, int]]:
        """get neighbor coordinates"""
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

        neighbors = set()
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                neighbors.add((i, j))
        neighbors.remove((row, col))
        return neighbors

    def execute_flips(self):
        """execute flips and reset update lists"""
        while self.flip_queue:
            self.flip_queue.pop()()

        self.update_list = self.future_update_list
        self.future_update_list = set()

    def step(self):
        """Perform a step of the game."""
        while self.update_list:
            row, col = self.update_list.pop()
            node = self.mat[row][col]
            # neighbors = self.num_neighbors(i, j)
            num_neighbors = sum(self.mat[i][j].alive for i, j in node.neighbors)
            if node.alive:
                if (num_neighbors <= 1) or (num_neighbors >= 4):
                    self.flip_node(row, col)
            else:
                if num_neighbors == 3:
                    self.flip_node(row, col)

        # Execute
        self.execute_flips()

        print(self)
