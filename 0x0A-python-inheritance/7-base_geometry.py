#!/usr/bin/python3
""" base geometry module """


class BaseGeometry():
    """ Base Geometr Class """

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """ returns area"""
        raise Exception("area() is not implemented")
