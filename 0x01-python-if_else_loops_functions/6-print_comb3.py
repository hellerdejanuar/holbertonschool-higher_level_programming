#!/usr/bin/python3
notfirst = False
for i in range(10):
    for j in range(i+1, 10):
        if notfirst:
            print(end=', ')
        else:
            notfirst = True
        print(f"{i}{j}", end='')
print()
