#!/usr/bin/python3

"""Python program that prints ASCII alphabets in lowercase except 'q' and 'e'."""

for letter in range(97, 123):
    if chr(letter) not in ['e', 'q']:
        print('{}'.format(chr(letter)), end='')
