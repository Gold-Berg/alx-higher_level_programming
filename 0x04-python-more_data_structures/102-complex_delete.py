#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    _delete = [key for key, v1 in a_dictionary.items() if v1 == value]
    for key in_delete:
        del a_dictionary[key]
        return a_dictionary
