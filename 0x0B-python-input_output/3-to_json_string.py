#!/usr/bin/python3
"""This module created a json dump file"""
import json


def to_json_string(my_obj):
    """This fuction serializes a json file.
    Args:
    my_obj: python to be dumped.
    """
    return(json.dumps(my_obj))
