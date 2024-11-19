#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def transpose(matrix):
    """ transposes the matrix in place """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    """ reverses the rows of the matrix"""
    n = len(matrix)
    for row in matrix:
        for i in range(n // 2):
            row[i], row[n - i - 1] = row[n - i - 1], row[i]


def rotate_2d_matrix(matrix):
    """
    rotates a nxn matrix clockwise 90 degrees
    need transpose first
    then reverse every row.
     """
    transpose(matrix)
    reverse_rows(matrix)
