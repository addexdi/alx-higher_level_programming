#!/usr/bin/python3
"""Module that inherites from python list class"""


class MyList(list):
    """MyList class that inherits from list and print list object in sorted order"""

    def print_sorted(self):
        """Function that prints list in sorted order"""
        print(sorted(self))
