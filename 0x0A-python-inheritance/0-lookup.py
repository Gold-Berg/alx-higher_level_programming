#!/usr/bin/python3
"""
A function that returns the list of available attributes/methods of an object:
"""


def lookup(obj):
    """
    Returns all obj in an obj dictionary as a list
    """

    return dir(obj)
