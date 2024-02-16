"""Module for defining node classes.
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Node:
    """Main node class."""

    alive: bool = False
    color_index: int = 0
    color_list: ClassVar[list[tuple[float, float, float]]] = [(0, 0, 0), (1, 1, 1)]

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
