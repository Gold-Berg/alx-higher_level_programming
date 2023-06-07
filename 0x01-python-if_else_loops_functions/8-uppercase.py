#!/usr/bin/python3
def uppercase(str):
    output_str = ''
    for char in str:
        uppercase_ = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        output_str += uppercase_
        print("{}".format(output_str))
