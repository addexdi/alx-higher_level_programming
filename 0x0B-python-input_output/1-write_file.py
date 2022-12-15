#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This function writes to a file
     Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written."""

    with open(filename, "w", encoding="utf-8") as f_obj:
        return f_obj.write(text)
