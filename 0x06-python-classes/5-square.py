#!/usr/bin/python3
""" Class Square """


class Square:
    """this class defines a square"""

    def __init__(self, size=0):
        """Initializes square"""
        self.size = size

    def area(self):
        """Calculates area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square with # """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """changes the size of a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
