#!/usr/bin/python3
""" my_list """


class MyList(list):
    """  Class MyList """

    def print_sorted(self):
        """ prints elements sorted """
        print(sorted(self))
