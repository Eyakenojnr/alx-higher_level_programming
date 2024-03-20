#!/usr/bin/python3
"""A script which;
- takes in GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]

    auth = HTTPBasicAuth(username, passwd)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
