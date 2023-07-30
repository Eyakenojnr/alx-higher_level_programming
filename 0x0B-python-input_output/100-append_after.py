#!/usr/bin/python3
"""Search and updates a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a given string in a file.

    Args:
        filename (str): Name of file to update.
        search_string (str): String to search for.
        new_string (str): String to update in file.
    """
    with open(filename, 'r') as a_file:
        lines = a_file.readlines()

    with open(filename, 'w') as a_file:
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write('{}'.format(new_string))
