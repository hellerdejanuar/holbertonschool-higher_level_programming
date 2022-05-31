#!/usr/bin/python3
""" deserializing """
import json

def load_from_json_file(filename):
    """ load JSON representation from filename """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(my_obj, f)
