#!/usr/bin/python3
"""
checks if obj is an instace
"""


def is_exact_instance(obj, class_type):
    """
    Return true if obj is an innstance else false

    """

    return isinstance(obj, class_type and type(obj) is class_type)
