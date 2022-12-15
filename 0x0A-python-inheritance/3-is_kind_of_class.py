#!/usr/bin/python3
"""Module contains function that checks for an instance of an object"""


def is_kind_of_class(obj, a_class):
    """Returns true if an object is an instance of a class
    Args:
    obj: python object to be checked.
    a_class: the class name
    """
    return (isinstance(obj, a_class))
