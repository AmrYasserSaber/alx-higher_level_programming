#!/usr/bin/python3
"""Return the dictionary description with simple data structure."""
import json


def class_to_json(obj):
    if isinstance(obj, (str, int, bool)):
        return obj

    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    if hasattr(obj, '__dict__'):
        data = {}
        for key, value in obj.__dict__.items():
            data[key] = class_to_json(value)
        return data
