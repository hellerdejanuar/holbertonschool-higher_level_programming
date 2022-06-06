#!/usr/bin/python3
""" base module """


class Base:
    """ base class for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """

        if id is not None:
            self.id = id
        else:
            Base.nb_obj_increm()
            self.id = Base.__nb_objects

    @property
    def nb_object(self):
        return self.__nb_objects

    @classmethod
    def nb_obj_increm(cls, n=1):
        cls.__nb_objects += n

    def int_validator(self, name, value, cond=None):
        """ validates an int
            takes name and value
            accepts condition to test for specific values"""

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if cond is not None:
            if cond == 'positive':
                if value <= 0:
                    raise ValueError(f"{name} must be > 0")
            elif cond == 'positiveOrZero':
                if value < 0:
                    raise ValueError(f"{name} must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string representation of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
