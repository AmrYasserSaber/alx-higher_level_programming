#!/usr/bin/python3
"""module for converting to json form"""
import json


def save_to_json_file(my_obj, filename):
    """convert the object to json"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
