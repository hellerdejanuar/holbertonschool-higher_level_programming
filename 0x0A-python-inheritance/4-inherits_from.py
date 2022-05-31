#!/usr/bin/python3
""" inherits module """


def inherits_from(obj, a_class):
    """ checks if object inherits attributes from a class """

    if isinstance(obj, a_class) and (type(obj) != a_class):
        return True
    else:
        return False
