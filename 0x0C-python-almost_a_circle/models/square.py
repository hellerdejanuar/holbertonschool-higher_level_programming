#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.classname}] ({self.id})"
                f" {self.__x}/{self.__y} - {self.__height}")
