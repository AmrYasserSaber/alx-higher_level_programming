#!/usr/bin/python3
"""textfile for writing files"""


def write_file(filename="", text=""):
    """writing a string to a text file (UTF8) and returning the number of
    characters written"""
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        return len(text)
