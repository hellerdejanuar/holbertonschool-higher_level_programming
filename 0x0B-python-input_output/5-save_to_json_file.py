#!/usr/bin/python3
""" deserializing """
import json


def save_to_json_file(my_obj, filename):
    """ write JSON representation of my_obj to filename """

    with open(filename, encoding="utf-8") as f:
        json.dump(my_obj, f)
