#!/usr/bin/python3
for j in range(ord('a'), ord('z')+1):
    if chr(j) != 'q' and chr(j) != 'e':
        print("{}".format(chr(j)), end="")
