#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for items in matrix:
        new_matrix.append([x ** 2 for x in items])
    return new_matrix
