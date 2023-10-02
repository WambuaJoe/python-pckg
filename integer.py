#!/usr/bin/python3
"""
Addd integer module
contains:
add_int function
"""
from b_test import my_log


@my_log
def add_int(a, b=5):
    """
    computes and returns the addition of 2 integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
