#!/usr/bin/python3.9

def uniq_add(my_list=[]):
    uniq_list = []
    sum = 0
    for element in my_list:
        if element not in uniq_list:
            uniq_list.append(element)
            sum += element
    return sum
