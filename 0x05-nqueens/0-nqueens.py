#!/usr/bin/python3
"""
nqueens solutions
solution will be a simple brute force solution
with an actual board and checking everything manuall

a possible optimisation is to simulate the board by having
possible positions
and
conflicting positions
"""
import sys


def find_ones_indices(arr):
    """ as name implies, returns array of them [i, j] """
    indices = []
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == 1:
                indices.append([i, j])
    return indices


def check_possible_move(board, row, col):
    """
    check if diagonals have a queen
    then check if  rows have a queen
    then check if cols have a queen
    up is row--
    down is row++
    left is col--
    right is col++
    """
    n = len(board)
    # check up and right
    temp_row = row
    temp_col = col
    while temp_row >= 0 and temp_col < n:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col += 1

    # check down and left
    temp_row = row
    temp_col = col
    while temp_row < n and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col -= 1

    # down and right
    temp_row = row
    temp_col = col
    while temp_row < n and temp_col < n:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row += 1
        temp_col += 1

    # up and left
    temp_row = row
    temp_col = col
    while temp_row >= 0 and temp_col >= 0:
        if board[temp_row][temp_col] == 1:
            return False
        temp_row -= 1
        temp_col -= 1

    temp_row = 0
    while temp_row < len(board):
        if board[temp_row][col] == 1:
            return False
        temp_row += 1

    temp_col = 0
    while temp_col < len(board[0]):
        if board[row][temp_col] == 1:
            return False
        temp_col += 1

    return True


def nqueens(board, current_column=0):
    """
    start from leftmost and go to the right
    """
    if current_column == len(board[0]):
        print(find_ones_indices(board))
        return True
    for i in range(0, len(board)):
        if check_possible_move(board, i, current_column):
            board[i][current_column] = 1
            nqueens(board[:], current_column + 1)
            board[i][current_column] = 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    if not sys.argv[1].isdigit():
        print('N must be a number')
        exit(1)
    if int(sys.argv[1]) < 4:
        print('N must be at least 4')
        exit(1)
    how_big = int(sys.argv[1])
    base_board = [[0] * how_big for _ in range(how_big)]
    nqueens(base_board)
