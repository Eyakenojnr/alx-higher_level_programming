#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON representation.
    Args:
        my_obj (str): Object to write to text file.
        filename (str): file to write to.
    """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
