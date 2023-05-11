#!/usr/bin/python3

if __name__ == "__main__":
    """Program that prints the number of and list of its
    arguments"""
    from sys import argv

    argv_len = len(argv) - 1
    digit = 1

    if argv_len == 0:
        print("{} arguments.".format(argv_len))
    elif argv_len == 1:
        print("{} argument:".format(argv_len))
        for arg in argv[1:]:
            print("{}: {}".format(digit, arg))
            digit += 1
    else:
        print("{} arguments:".format(argv_len))
        for arg in argv[1:]:
            print("{}: {}".format(digit, arg))
            digit += 1
