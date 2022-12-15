#!/usr/bin/python3.9

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    items = list(a_dictionary.items())
    items = [(i[1], i[0]) for i in items]
    items.sort()
    items = [(i[0], i[1]) for i in items]
    new_dict = items[-1][1]
    return new_dict
