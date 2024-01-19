#!/usr/bin/python3
"""Defines The Function That Add The New Attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Function To Add New Attribute If It Possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
