#!/usr/bin/python3
""" My integer module """


class MyInt(int):
    """ my class of integers """

    def __eq__(self, other):
        """ returns true when compared to other thing """
        return (self is other)

    def __ne__(self, other):
        """ returns false when compared to same  """
        return not (self is other)
