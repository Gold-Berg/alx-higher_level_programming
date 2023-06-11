#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Fill missing values with 0 if a tuple is smaller than 2
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    if len(tuple_a) == 2 and len(tuple_b) == 0:
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return result
