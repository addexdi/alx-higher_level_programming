#!/usr/bin/python3.9

def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary)
    for key in sorted_list:
        print('{}: {}'.format(key, a_dictionary[key]))
    return None
