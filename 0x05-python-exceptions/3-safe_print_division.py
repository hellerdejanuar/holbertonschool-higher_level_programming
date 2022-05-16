#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        n = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    else:
        print("Inside result: {:.0f}".format(n))
        return n
