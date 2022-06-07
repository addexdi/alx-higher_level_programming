#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    elem_2_mul = [x * y for x, y in my_list]
    elem_2_div = [y for x, y in my_list]
    total, no_of_element = 0.0, 0.0
    for i in range(len(my_list)):
        total += elem_2_mul[i]
        no_of_element += elem_2_div[i]
    return total / no_of_element
