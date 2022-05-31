#!/usr/bin/python3
""" write file module """


def write_file(filename="", text=""):
    """ writes a string to a file """
    
    if not filename:
        raise Exception('No file')

    with open(filename, w, encoding="utf-8") as f:
       f.write(text)
