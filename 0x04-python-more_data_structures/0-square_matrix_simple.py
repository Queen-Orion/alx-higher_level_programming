#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.

    """
    return list(map(lambda newMatrix: list(map(lambda v: v*v, newMatrix)),
                    matrix))
