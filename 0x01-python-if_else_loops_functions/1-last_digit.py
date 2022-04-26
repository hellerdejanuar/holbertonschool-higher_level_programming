#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])

if lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")

elif number > 0:
    print(f"Last digit of {number} is {lastdigit}", end='')
    if lastdigit < 6:
        print(f" and is less than 6 and not 0")
    else:
        print(f" and is greater than 5")

elif number < 0:
    print(f"Last digit of {number} is -{lastdigit} and \
is less than 6 and not 0")
