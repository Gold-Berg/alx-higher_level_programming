#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    _delete = [key for key, vl in a_dictionary.items() if vl == value]
    for key in _delete:
        del a_dictionary[key]
    return a_dictionary
