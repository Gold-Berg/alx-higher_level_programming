#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in my_list:
        try:
            print("{:d}".format(i))
            num += 1
            if num == x:
                break
            except (ValueError, TypeError, IndexError):
                pass
    return num
