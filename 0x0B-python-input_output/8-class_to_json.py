#!/usr/bin/python3
""" class to JSON module """


def class_to_json(obj):
    """ returns a dictionary descrption of an object in JSON format """

    return (obj.__dict__)
