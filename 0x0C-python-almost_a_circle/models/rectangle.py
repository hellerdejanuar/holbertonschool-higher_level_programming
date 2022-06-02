#!/usr/bin/python3
""" rectangle module """
from models.base import Base
from models.util import int_valid

class Rectangle(Base):
    """ rectangle class. inherits id management from Base
    needs width & height
    accepts x,y coordinates """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes Rectangle """
        super().__init__(id)

        int_valid('width', width, 'positive')
        int_valid('height', height, 'positive')
        int_valid('x', x, 'positiveOrZero')
        int_valid('y', y, 'positiveOrZero')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Width
    @property
    def width(self):
        """ retrieves width """
        return self.__width
    @width.setter
    def width(self, width):
        """ sets width """
        int_valid('width', width, 'positive')
        self.__width = width

    # Height
    @property
    def height(self):
        """ retrieves height """
        return self.__height
    @height.setter
    def height(self, height):
        """ sets height """
        int_valid('height', height, 'positive')
        self.__height = height

    # X
    @property
    def x(self):
        """ retrieves x """
        return self.__width
    @x.setter
    def x(self, x):
        """ sets x """
        int_valid('x', x, 'positiveOrZero')
        self.__x = x

    # Y
    @property
    def y(self):
        """ retrieves y """
        return self.__y
    @y.setter
    def y(self, y):
        """ sets y """
        int_valid('y', y, 'positiveOrZero')
        self.__y = y
