#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for row in new_matrix:
        for elemn in new_matrix:
            elem = elem * elem
