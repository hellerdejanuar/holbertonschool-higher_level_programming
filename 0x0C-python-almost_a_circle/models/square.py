#!/usr/bin/python3
""" square module """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    classname = "Square"

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.classname}] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__height}")
    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size Setter """
        self.width = value
        self.height = value
