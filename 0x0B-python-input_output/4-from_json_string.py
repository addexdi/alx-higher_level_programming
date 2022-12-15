#!/usr/bin/python3
"""This module deserializes a json dump file"""
import json


def from_json_string(my_str):
    """This fuction deserializes a json file.
    Args:
    my_obj: python to be dumped.
    """
    return(json.loads(my_str))
