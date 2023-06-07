#!/usr/bin/python3
def uppercase(str):
    for char in str:
        uppercase_ = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        print("{}".format(uppercase_), end='')
        print()
