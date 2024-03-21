#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository "rails" by the user "rails"
All commits are printed by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    commits = r.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass

"""
// Alternative to the try block //

for commit in commits:
    sha = commit['sha']
    author_name = commit['commit']['author']['name']
    print(f"{sha}: {author_name}")
"""
