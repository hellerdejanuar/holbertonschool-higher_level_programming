#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for index in range(row_len):
            print(row[index], end='')
            if index != row_len - 1:
                print(end=' ')
        print()
