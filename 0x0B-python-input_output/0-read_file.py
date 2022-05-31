#!/usr/bin/python3
""" read file module """


def read_file(filename=""):
    """ reads a file and prints it to stdout """

    with open(filename, encoding="utf-8") as f:
       print(f.read())
