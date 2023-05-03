#!/usr/bin/python3

def uppercase(str):
    uppercase_string = ''
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char_code = ord(char) - ord('a') + ord('A')
            uppercase_char = chr(uppercase_char_code)
        else:
            uppercase_char = char
        uppercase_string += uppercase_char
    print("{}".format(uppercase_string))
