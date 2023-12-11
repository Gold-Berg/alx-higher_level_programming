#!/usr/bin/python3
"""
a function that returns True if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if it's an instance else false
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
