#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

if __name__ == '__main__':
    import sys
    save_to_json_file = __import__('5-save_to_json_file')\
            .save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    try:
        # Load existing list from file
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # Create a new list if the file doesn't exist
        items = []

    # Add arguments to the list
    items.extend(sys.argv[1:])
    # Save the updated list to the file
    save_to_json_file(items, 'add_item.json')
