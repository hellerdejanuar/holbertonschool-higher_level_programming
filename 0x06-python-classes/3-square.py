#!/usr/bin/python3
""" Class Square """


class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        """initializes a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of square"""
        return size * size
