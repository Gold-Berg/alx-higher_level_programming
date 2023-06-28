#!/usr/bin/python3
""" bytecode interpretation"""
import math
""" import math mordule"""
class MagicClass:
    """ magicclass class """


    def __init__(self, radius):
        """ instances of class """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """ returns area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ returns circumfrence """
        return 2 * math.pi * self.__radius
