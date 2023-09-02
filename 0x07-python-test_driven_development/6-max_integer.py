#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(l=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(l) == 0:
        return None
    result = l[0]
    i = 1
    while i < len(l):
        if l[i] > result:
            result = l[i]
        i += 1
    return result
