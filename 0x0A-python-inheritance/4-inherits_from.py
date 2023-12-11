#!/usr/bin/python3
"""
returns True if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    def is_kind_of_class(obj, a_class): else false
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
