#!/usr/bin/python3
""" serializing """

def to_json_string(my_obj):
    """ converts JSON representation of an object """

    if not my_obj:
        raise Exception('No object')

    with open(filename, 'a', encoding="utf-8") as f:
        ch_cn = f.write(text)
    return ch_cn
