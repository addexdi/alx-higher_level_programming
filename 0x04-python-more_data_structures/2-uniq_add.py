#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for num in set(my_list):
        add += num
    return add
