#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            print("Fzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz ")
        else:
            print(f"{num} ", end="")
