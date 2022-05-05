#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary:
        new_dict.update({key:value * 2})
    return new_dict
