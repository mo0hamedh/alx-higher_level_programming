#!/usr/bin/python3
"""Check If Obj Is Instance Of Class"""


def inherits_from(obj, a_class):
    """Check Function"""
    return isinstance(obj, a_class) and type(obj) != a_class
