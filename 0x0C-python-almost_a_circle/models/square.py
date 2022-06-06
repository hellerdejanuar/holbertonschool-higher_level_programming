#!/usr/bin/python3
""" square module """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    classname = "Square"
    attrs = ["id", "size", "x", "y"]

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[{self.classname}] ({self.id})"
                f" {self.x}/{self.y} - {self.height}")

    def update(self, *args, **kwargs):
        """ updates attributes based on incoming args """

        if args:
            for i in range(len(args)):
                setattr(self, self.attrs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ returns dict representation of object """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}


    @property
    def size(self):
        """ retrieves size (width) """
        return self.width

    @size.setter
    def size(self, size):
        """ sets height and width """
        self.width = size
        self.height = size
