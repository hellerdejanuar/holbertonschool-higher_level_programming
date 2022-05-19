#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """this class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle"""
        self.height = height
        self.width = width

    def __str__(self):
        return f"{'#' * self.height}"

    def area(self):
        """Calculates area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of rectangle"""
        return (self.__width + self.__height) * 2

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """changes the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """changes the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
