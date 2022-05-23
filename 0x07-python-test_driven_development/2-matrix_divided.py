#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for i, elem in enumerate(row):
            if not isinstance(elem, (int, float))
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif isinstance(elem, bool)
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if el_cn == 0:
            el_cn = i
        elif el_cn != i:
            raise TypeError("Each row of the matrix must have the same size")


