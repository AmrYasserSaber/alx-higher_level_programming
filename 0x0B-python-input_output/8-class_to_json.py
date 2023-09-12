#!/usr/bin/python3
"""Return the dictionary description with simple data structure."""
import json


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
    return obj.__dict__
