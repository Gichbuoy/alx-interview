#!/usr/bin/python3
"""
Rotate a 2D matrix in place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.

    Parameters:
    matrix (List[List[int]]): The input 2D matrix to be rotated.
    """
    old = []
    for i in matrix:
        old.append(i.copy())
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[j][i] = old[n - i - 1][j]
