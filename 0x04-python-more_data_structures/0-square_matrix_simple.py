#!/usr/bin/python3.9

def square_matrix_simple(matrix=[]):
    matrix_out = [[ele**2 for ele in row]for row in matrix]
    return matrix_out
