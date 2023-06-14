#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman= {
            'I': 1,
            'W': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    res = 0
    prev_value = 0

    for charin roman_string[::-1]:
        value = roman_values.get(char, 0)
        if value >= prev_value:
            res += value
        else:
            res -= value
        prev_value = value

   return res
