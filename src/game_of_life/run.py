"""Main script to run the game of life.
"""

from game_of_life.grid import Grid


def main() -> int:
    """Main function."""

    grid = Grid(10, 10)
    grid.mat[1][2].flip()
    grid.mat[2][3].flip()
    grid.mat[3][1].flip()
    grid.mat[3][2].flip()
    grid.mat[3][3].flip()
    return 0


if __name__ == "__main__":
    main()
