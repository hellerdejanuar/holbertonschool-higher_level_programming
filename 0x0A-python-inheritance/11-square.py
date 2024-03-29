#!/usr/bin/python3
""" square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ instatiate """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns area """
        return (self.__size * self.__size)

    def __str__(self):
        """ returns the descritpion of the square """
        return (f"[Square] {self.__size}/{self.__size}")
