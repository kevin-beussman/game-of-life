"""Main script to run the game of life.
"""

from game_of_life.grid import Grid


def main() -> int:
    """Main function."""

    grid = Grid(10, 10)
    grid.initialize_nodes(
        [
            (1, 2),
            (2, 3),
            (3, 1),
            (3, 2),
            (3, 3)
        ]
    )
    print(grid)
    
    return 0


if __name__ == "__main__":
    main()
