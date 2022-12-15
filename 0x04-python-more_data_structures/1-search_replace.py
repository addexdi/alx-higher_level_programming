#!/usr/bin/python3.9

def search_replace(my_list, search, replace):
    result = [replace if elements ==
              search else elements for elements in my_list]
    return result
