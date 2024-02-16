"""Main script to run the game of life.
"""

from game_of_life.nodes import Node


def main() -> int:
    """Main function."""

    rows = 10
    cols = 10

    grid = [[Node() for _ in range(cols)] for _ in range(rows)]
    print(grid)
    return 0


if __name__ == "__main__":
    main()
