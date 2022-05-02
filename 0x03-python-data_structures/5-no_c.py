#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    i = 0
    new_string = ""

    while i < str_len:
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            new_string += my_string[i]
        i += 1
    return (new_string)
