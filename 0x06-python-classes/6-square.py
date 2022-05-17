#!/usr/bin/python3
""" Class Square """


class Square:
    """this class defines a square"""

    def __init__(self, size=0, position=(0,0)):
        """Initializes square"""
        self.size = size
        self.position = position

    def area(self):
        """Calculates area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square with # """
        if self.size == 0:
            print()
            return

        if self.position[1] > 0:
            for lines in range(self.position[1]):
                print()
        for i in range(self.size):
            for spaces in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#",end="")
            print()

    @property
    def size(self):
        """retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """changes the size of a square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property 
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """changes position of square, receives (x,y) tuple"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
