#!/usr/bin/python3
"""This module writes to a file from JSON rep"""
import json


def load_from_json_file(filename):
    """This fuction write an python obj from a json file.
    Args:
    filename: name of th file(.json)
    """
    with open(filename) as f_obj:
        return json.load(f_obj)
