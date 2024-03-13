#!/usr/bin/python3
"""A script which;
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Get URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Parse and encode data to be sent in the POST request
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")

    # Creating Request object
    req = urllib.request.Request(url, data)

    # Sending the request and getting the response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
