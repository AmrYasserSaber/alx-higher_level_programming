#!/usr/bin/python3
"""Return the dictionary description with simple data structure."""
import json


class MyClass:
    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

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
