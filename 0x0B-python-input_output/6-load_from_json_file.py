#!/usr/bin/python3
"""module to create an object from a json file"""
import json

def load_from_json_file(filename):
    """loads from json file"""
    with open(filename, 'r') as f:
        return json.load(f)
