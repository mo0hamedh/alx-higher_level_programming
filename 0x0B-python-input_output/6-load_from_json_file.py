#!/usr/bin/python3
"""Define The Function That Create An Object From JSON File"""
import json


def load_from_json_file(filename):
    """Function That Create An Object"""
    with open(filename) as file:
        return json.load(file)
