#!/usr/bin/python3
def uniq_add(my_list=[]):
    unq = set()

    for i in my_list:
        if i not in unq:
            unq.add(i)

    total = sum(unq)

    return total
