#!/usr/bin/python3

def max_integer(my_list=[]):
    top1 = 0

    if not my_list:
        return None

    for num in my_list:
        if top1 < num:
            top1 = num

    return (top1)
