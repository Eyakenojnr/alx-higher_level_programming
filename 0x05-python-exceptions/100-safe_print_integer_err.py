#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    tag = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        tag = False
        print("Exception: {}".format(err), file=sys.stderr)

    return tag
