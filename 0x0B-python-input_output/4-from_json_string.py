#!/usr/bin/python3
""" deserializing """
import json


def from_json_string(my_str):
    """ converts string to JSON representation """

    return(json.loads(my_str))
