#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    track = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            track += 1
            if track == x:
                break
        except (ValueError, TypeError):
            pass
    print()
    return track
