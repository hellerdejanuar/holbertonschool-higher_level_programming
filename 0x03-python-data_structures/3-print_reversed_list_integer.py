#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list)

    for index in range(list_len - 1, -1, -1):
        print(my_list[index])
