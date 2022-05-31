#!/usr/bin/python3
""" same class module """


def is_same_class(obj, my_type):
    """ checks if object is the same as the specified class """
    
    if type(obj) == my_type:
        return True
    else: 
        return False
