#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for elem in new_list:
        if elem == replace:
            elem = replace
    return new_list
