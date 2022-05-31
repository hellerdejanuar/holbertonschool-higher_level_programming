#!/usr/bin/python3
""" is kind module """


def is_kind_of_class(obj, a_class):
    """ checks if is class or sublcass """

    if isinstance(obj, a_class):
        return True
    else:
        return False
