#!/usr/bin/python3.9

def multiply_by_2(a_dictionary):
    d = {}
    for key in a_dictionary:
        if key not in d:
            d[key] = (a_dictionary[key]) * 2
    return d
