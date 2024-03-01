#!/bin/bash
# Takes in a URL sends a request to that URL and displays the size of the body
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

BODY_SIZE=$(curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}')

echo "$BODY_SIZE"
