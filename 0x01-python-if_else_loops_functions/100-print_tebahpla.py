#!/usr/bin/python3
switch = False
for letter in range(25, -1, -1):
    if switch:
        letter = letter + 65
        switch = False
    else:
        letter = letter + 97
        switch = True
    print(chr(letter), end='')
