#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            res = 0
            if i < len(my_list_1) and i < len(my_list_2):
                res = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new.append(res)
    return new
