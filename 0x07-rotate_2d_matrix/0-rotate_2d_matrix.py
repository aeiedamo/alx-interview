#!/usr/bin/python3
"""
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
        rotate a n x n matrix
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)
