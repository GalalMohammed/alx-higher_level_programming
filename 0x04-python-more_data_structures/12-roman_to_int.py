#!/usr/bin/python3
def roman_to_int(roman_string):
    converted_int = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string and type(roman_string) == type(""):
        for c in roman_string:
            temp = converted_int % roman[c]
            converted_int = (converted_int - temp) + roman[c] - temp
    return converted_int
