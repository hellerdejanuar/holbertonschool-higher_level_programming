#!/usr/bin/python3
""" append to file module """


def append_write(filename="", text=""):
    """ appendss a string to a file """

    if not filename:
        raise Exception('No file')

    with open(filename, 'a', encoding="utf-8") as f:
        ch_cn = f.write(text)
    return ch_cn
