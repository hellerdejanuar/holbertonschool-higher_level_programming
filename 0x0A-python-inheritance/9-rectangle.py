#!/usr/bin/python3
""" base geometry module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """ instatiate """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns area """
        return (width * height)

    def __str__(self):
        """ returns the descritpion of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")
