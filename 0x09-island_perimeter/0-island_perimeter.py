#!/usr/bin/python3
"""
island_perimeter module
"""
def count_perimeter(grid, row, col):
    count = 0
    above = row - 1
    below = row + 1
    right = col + 1
    left = col - 1
    if 0 <= above < len(grid):
        if grid[above][col] == 0:
            count += 1
            # grid[above][col] = 2
    if 0 <= below < len(grid):
        if grid[below][col] == 0:
            count += 1
            # grid[below][col] = 2
    if 0 <= right < len(grid[0]):
        if grid[row][right] == 0:
            count += 1
            # grid[row][right] = 2
    if 0 <= left < len(grid[0]):
        if grid[row][left] == 0:
            count += 1
            # grid[row][left] = 2
    return count


def island_perimeter(grid):
    """
    0 is water 1 is land
    """
    ret = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                ret += count_perimeter(grid, i, j)
    return ret
