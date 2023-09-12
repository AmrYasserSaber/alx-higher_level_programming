#!/usr/bin/python3
"""textfile for reading files"""


def read_file(filename=""):
    """reading an entire file and printing its content"""
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
