#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def append_write(filename="", text=""):
    """This function appends to a file
    Args:
    filename: filepath.
    text: string to be appended.
    """
    with open(filename, "a+", encoding="utf-8") as f_obj:
        return f_obj.write(text)
