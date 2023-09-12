#!/usr/bin/python3
"""Return the dictionary description with simple data structure."""
import json


def class_to_json(obj):
    # Get the class attributes and their values
    attributes = obj.__dict__

    # Initialize a dictionary to store the JSON-serializable representation
    json_dict = {}

    for key, value in attributes.items():
        # Check if the value is a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
