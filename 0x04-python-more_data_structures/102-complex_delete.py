#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    _delete = []
    for key, v1 in a_dictionary.iterms():
        if v1 == value:
            _delete.append(key)
    for key in _delete:
        del a_dictionary[key]
    return a_dictionary
