#!/usr/bin/python3

if __name__ == "__main__":
    """Print result of the addition of all arguments"""
    import sys

    total = 0
    for i in sys.argv[1:]:
        total += int(i)
    print(total)
