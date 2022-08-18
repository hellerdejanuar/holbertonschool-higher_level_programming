#!/bin/bash
# parses the specified parameter from the request header. needs the ip as argument

curl -s -I /dev/null "$1" | grep  "Content-Length: " | sed 's/^.*: //'
