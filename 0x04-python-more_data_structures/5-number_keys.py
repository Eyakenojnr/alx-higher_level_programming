#!/usr/bin/python3

def number_keys(a_dictionary):
    count = lambda x: len(x.keys())
    return count(a_dictionary)
