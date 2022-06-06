#!/usr/bin/python3
""" rectangle module """
from models.base import Base
from models.util import int_valid


class Rectangle(Base):
    """ rectangle class. inherits id management from Base
    needs width & height
    accepts x,y coordinates """

    classname = "Rectangle"

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

    def area(self):
        """ returns area """
        return self.__width * self.__height

    def display(self):
        """ a rectangle of # """
        print("\n" * self.__y, end="")
        print(f"{' ' * self.__x}{'#' * self.__width}\n" * self.height, end="")

    def __str__(self):
        """ description of the object """
        return (f"[{self.classname}] ({self.id})"
        f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args):
        """ updates attributes based on incoming args """
        argc = len(args)

        if argc >= 1:
            self.id = args[0]
        if argc >= 2:
            self.__width = args[1]
        if argc >= 3:
            self.__height = args[2]
        if argc >= 4:
            self.__x = args[3]
        if argc >= 5:
            self.__y = args[4]

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
