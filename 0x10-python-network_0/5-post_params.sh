#!/bin/bash
# parses the specified parameter from the request header. needs the ip as argument
curl -s -X POST -H "email:test@gmail.com" -H "subject:test@gmail.com" "$1"
