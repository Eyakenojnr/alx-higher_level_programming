#!/usr/bin/python3
"""A script which;
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
