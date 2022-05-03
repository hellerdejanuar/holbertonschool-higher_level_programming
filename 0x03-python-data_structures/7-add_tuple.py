#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_ar = [tuple_a, tuple_b] 
    i = 0 # tuple iterator
    j = 0 # variable iterator
    result = [0, 0] # array to store the sum

    for tupl in tuple_ar:
        j = 0 
        for var in tupl:
            result[j] += var
            j += 1
        i += 1

    result_tpl = (result[0], result[1])

    return (result_tpl)
