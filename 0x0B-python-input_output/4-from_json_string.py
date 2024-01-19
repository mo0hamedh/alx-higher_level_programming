#!/usr/bin/python3
"""Function That Returns an Object By JSON String"""
import json


def from_json_string(my_str):
    """Convert Function"""
    return json.loads(my_str)
