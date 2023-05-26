#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    return sum([element for element in uniq_list])
