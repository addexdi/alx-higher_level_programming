#!/usr/bin/python3
"""This function reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """This function parses a txt file
    Args:
    @filename: name of the file to be parsed
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
