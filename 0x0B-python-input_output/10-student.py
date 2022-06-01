#!/usr/bin/python3
""" student module """


class Student:
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """ init student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dict of object attributes """
        if isinstance(attrs, list):
            if all(isinstance(elem, str) for elem in attrs):
                dic = {}
                for att in attrs:
                    if att in self.__dict__.keys():
                        dic[att] = self.__dict__[att]
                return dic
        else:
            return(self.__dict__)
