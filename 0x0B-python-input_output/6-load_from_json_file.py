#!/usr/bin/python3
"""module for def load from json file method"""


import json


def load_from_json_file(filename):
    """that creat an object from a “JSON file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
