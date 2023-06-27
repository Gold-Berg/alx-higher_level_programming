#!/usr/bin/python3
""" Module of a square class """


class Square:
    """ Square class """

    def __init__(self, size=0):
        """ Square instance with optional size """

        self.__size = size

    @property
    def size(self):
        """ Returns the size of a square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size of the square """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates area of a square  """
        return self.__size * self.__size
