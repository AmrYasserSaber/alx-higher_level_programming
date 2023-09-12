#!/usr/bin/python3
"""" module for converting from json form"""
import json


def from_json_string(my_str):
    """convert the object from json"""
    return json.loads(my_str)
