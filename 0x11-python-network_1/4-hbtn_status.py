#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status and displays
the web page type and content.
"""

if __name__ == '__main__':
    import requests

    # Creating a Response object
    r = requests.get('https://alx-intranet.hbtn.io/status')

    # Print body response
    print("Body response:")
    print(f"\t- type: {r.text.__class__}")
    print(f"\t- content: {r.text}")
