#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev = roman_string[0]
    sum_int = roman_map.get(prev)
    for s in roman_string.upper()[1:]:
        if roman_map.get(s) <= roman_map.get(prev):
            sum_int += roman_map.get(s)
        else:
            sum_int += (roman_map.get(s) - 2 * roman_map.get(prev))
        prev = s
    return sum_int
