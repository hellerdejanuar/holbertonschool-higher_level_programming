#!/usr/bin/python3
""" This modlue operates matrixes """

def _raiseError(errCode):
    """ raises error based on string """
    if errCode == "zero":
        raise ZeroDivisionError("division by zero")

    elif errCode == "dif_len":
        raise TypeError("Each row of the matrix must have the same size")
    
    elif errCode == "not_matrix":
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    elif errCode == "not_div":
        raise TypeError("div must be a number")
    
    else:
        raise NameError("error code not found")


def matrix_divided(matrix, div):
    """ divides a matrix between div """

    new_matrix = []

    if not isinstance(matrix, list):
        _raiseError("not_matrix")
    try:
        first_row_len = len(matrix[0])
    except:
        _raiseError("not_matrix")


    if not isinstance(div, (int, float)):
        _raiseError("not_div")
    if div == 0:
        _raiseError("zero")


    for i, row in enumerate(matrix):

        if not isinstance(row, list):
            _raiseError("not_matrix")
        else:
            new_matrix.append([])

        for elem in row:

            if not isinstance(elem, (list, float)):
                _raiseError("not_matrix")
            else:
                new_matrix[i].append(elem)

    return new_matrix
