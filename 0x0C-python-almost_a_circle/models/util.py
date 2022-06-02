#!/usr/bin/python3
""" utilities module """


def int_valid(name, value, cond=None):
    """ validates an int 
        takes name and value
        accepts condition to test for specific values"""
        
    if type(value) != int:
        raise TypeError(f"{name} must be an integer")

    if cond != None:
        if cond == 'positive':
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        elif cond == 'positiveOrZero':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
