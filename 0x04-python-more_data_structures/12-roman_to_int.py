#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_val = 0

    for numeral in reversed(roman_string):
        value = rom_num.get(numeral, 0)

        if value < prev_val:
            total = total - value
        else:
            total = total + value

        prev_val = value

    return total
