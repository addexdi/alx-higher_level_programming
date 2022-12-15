#!/usr/bin/python3
"""Look up modules"""


def lookup(obj):
    """This function acts a look up table for python objects.
    Args:
    obj: python object to be looked up.
    """
    return dir(obj)
