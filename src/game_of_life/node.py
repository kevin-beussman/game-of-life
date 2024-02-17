"""Module for defining node classes.
"""

from dataclasses import dataclass, field
from typing import ClassVar, Self


@dataclass
class Node:
    """Main node class."""

    row: int
    col: int
    alive: bool = False
    color_index: int = 0
    color_list: ClassVar[list[tuple[float, float, float]]] = [(0, 0, 0), (1, 1, 1)]
    neighbors: set[tuple[int, int]] = field(default_factory=set)

    @property
    def num_colors(self):
        """Number of defined colors.

        Returns:
            int: Number of defined colors.
        """
        return len(self.color_list)

    def flip(self) -> None:
        """Flip the state of the node and increment the color."""
        self.alive = not self.alive
        self.color_index = (self.color_index + 1) % self.num_colors
