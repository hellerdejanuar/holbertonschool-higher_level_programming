#!/usr/bin/python3
first = False
for i in range(10):
    for j in range(i+1, 10):
        if first:
            print(end=', ')
        else:
            first = True
        print(f"{i}{j}", end='')
print()
