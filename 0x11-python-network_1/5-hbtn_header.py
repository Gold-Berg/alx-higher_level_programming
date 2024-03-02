#!/usr/bin/env python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    print(response.headers.get('X-Request-Id'))

