#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_len = len(my_list)
        
        if len(my_list) == 0:
            for index in range(list_len - 1, -1, -1):
                print(my_list[index])
