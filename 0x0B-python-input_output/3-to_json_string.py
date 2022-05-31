#!/usr/bin/python3
""" serializing """
import json


def to_json_string(my_obj):
    """ converts JSON representation of an object """

    return(json.dumps(my_obj))
