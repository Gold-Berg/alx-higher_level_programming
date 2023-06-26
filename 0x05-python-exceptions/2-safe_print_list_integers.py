#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    track = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            track += 1
        except (ValueError, TypeError):
            i -= 1
        except IndexError:
            pass
    print()
    return track
