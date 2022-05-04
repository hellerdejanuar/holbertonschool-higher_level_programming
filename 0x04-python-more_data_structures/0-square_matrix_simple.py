#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i, row in enumerate(matrix):
        new_matrix.append([])
        for j, elem in enumerate(row):
            new_matrix[i].append(row[j] * row[j])

    return new_matrix
