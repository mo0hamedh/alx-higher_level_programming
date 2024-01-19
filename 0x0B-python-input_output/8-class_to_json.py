#!/usr/bin/python3
"""Define Function That Convert Class To JSON"""


def class_to_json(obj):
    """Function That Convert Class To JSON"""
    return obj.__dict__
