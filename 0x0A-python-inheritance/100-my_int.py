#!/usr/bin/python3
"""Module for MyInt"""


class MyInt(int):
    """This class inherits from the python int object class"""

    def __eq__(self, obj):
        """special equal method"""
        if self.real == obj:
            return False

    def __ne__(self, obj):
        """Not equal dunder method"""
        return not self.__eq__(obj)
