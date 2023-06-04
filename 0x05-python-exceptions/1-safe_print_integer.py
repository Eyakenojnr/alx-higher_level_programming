#!/usr/bin/python3

def safe_print_integer(value):
    tag = True
    try:
        print("{:d}".format(value))
    except:
        tag = False
    return tag
