#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    converts a roman numeral to an integer.

    """
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    numerals = list(map(lambda x: roman_nums.get(x), roman_string))
    result = 0
    for i, value in enumerate(numerals):
        if i <= len(numerals) - 2 and value < numerals[i + 1]:
            result -= value
        else:
            result += value
    return result
