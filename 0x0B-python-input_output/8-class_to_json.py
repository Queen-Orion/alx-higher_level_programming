#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """returns dict description of obj"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return{}
