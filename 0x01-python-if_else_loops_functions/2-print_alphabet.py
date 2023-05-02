#!/usr/bin/python3

"""Print English alphabet in lowercase, not followed by a new line."""

for letter in range(ord('a'), ord('z')+1):
    print(chr(letter), end='')
