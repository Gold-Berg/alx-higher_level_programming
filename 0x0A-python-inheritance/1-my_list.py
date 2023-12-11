#!/usr/bin/python3
"""
class List that inherits from list
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """
        print the list in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
