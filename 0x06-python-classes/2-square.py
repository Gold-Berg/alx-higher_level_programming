#!/usr/bin/python3
""" Module of a square """


class Square:
    """ Represents a square class """
    def __init__(self, size=0):
        """ Square instance with optional size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
