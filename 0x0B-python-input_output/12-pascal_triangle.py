#!/usr/bin/python3
""" pascal triangle module """


def pascal_triangle(n):
    """ createas a pascal triangle of size n """

    if n <= 0:
        return []

    pascal = []
    for row_n in range(n):
        pascal.append([])

        if row_n == 0:
            pascal[row_n].append(1)

        else:
            for elem_n in range(row_n + 1):

                prev_row = pascal[row_n - 1]

                if elem_n == 0:
                    el_sum = prev_row[0]
                elif elem_n == row_n:
                    el_sum = prev_row[row_n - 1]
                else:
                    el_sum = prev_row[elem_n - 1] + prev_row[elem_n]

                pascal[row_n].append(el_sum)

    return pascal
