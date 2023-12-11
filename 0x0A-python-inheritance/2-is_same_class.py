#!/usr/bin/python3
"""
checks if obj is an instace
"""


def is_exact_instance(obj, class_type):
    """
    Returns True if the object is exactly an instance else False.
    """
    return isinstance(obj, class_type) and type(obj) is class_type
