#!/usr/bin/python3
switch = False
for letter in range(26,0):
    if switch:
        letter = letter + 65
        switch = False
    else:
        letter = letter + 97
        switch = True
    print(letter, end='')
