#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_ar = [tuple_a, tuple_b]
    tp_i = 0  # tuple iterator
    va_i = 0  # variable iterator
    result = [0, 0]  # array to store the sum

    for tupl in tuple_ar:
        va_i = 0

        for elem in tupl:
            if va_i >= len(result):
                break

            result[va_i] += elem
            va_i += 1

        tp_i += 1

    result_tpl = (result[0], result[1])

    return (result_tpl)
