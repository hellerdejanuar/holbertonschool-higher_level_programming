#!/usr/bin/python3
flag = False

for i in range(100):
    if i == 99:
        print(99)
    else:
        print(f'{i:02}', end=', ')
