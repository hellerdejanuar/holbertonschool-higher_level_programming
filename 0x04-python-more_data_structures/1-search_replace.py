#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return None

    new_list = my_list.copy()

    for elem in new_list:
        if elem == replace:
            elem = replace
    return new_list
