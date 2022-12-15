#!/usr/bin/python3
"""This module writes to a file using JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """This fuction deserializes a json file.
    Args:
    my_obj: python object.
    filename: name of th file(.json)
    """
    with open(filename, "w") as f_obj:
        json.dump(my_obj, f_obj)
