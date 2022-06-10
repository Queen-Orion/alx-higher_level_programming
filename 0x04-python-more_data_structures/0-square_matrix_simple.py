#!/usr/bin/python3
"""
computes the square value of all integers of a matrix.
Args: 
    matrix: 2D list to perform operation on
Return:
    same size and square of all value of a matrix
"""


def square_matrix_simple(matrix=[]):
    new_list = []
    for items in matrix:
        new_list.append(list(map(lambda X: X ** 2, items)))
        return new_list
