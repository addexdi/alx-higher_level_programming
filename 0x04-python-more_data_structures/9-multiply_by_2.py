#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.keys()
    return dict(zip(a, [x * 2 for x in a_dictionary.values()]))
