#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listt in matrix:
        for num in listt:
            if listt[len(listt)-1] != num:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num))
