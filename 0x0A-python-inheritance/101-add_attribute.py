#!/usr/bin/python3
""" Add attribute module """


def add_attribute(obj, name, value):
    """ adds new attribute to an object if possible """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
