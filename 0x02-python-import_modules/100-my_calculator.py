#!/usr/bin/python3

if __name__ == "__main__":
    """Import all functions from <calculator_1.py> and handle basic
    operations."""
    import sys
    from calculator_1 import add, sub, mul, div

    # If number of arguments is not 3, print usage to stderr and exit
    args = len(sys.argv) - 1
    if args != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    legible_operator = ['+', '-', '*', '/']
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # If invalid operator is passed, print error message to stderr and exit
    if operator not in legible_operator:
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
