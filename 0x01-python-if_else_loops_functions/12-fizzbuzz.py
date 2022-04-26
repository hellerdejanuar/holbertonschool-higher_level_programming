#!/usr/bin/python3
def fizzbuzz():
    for i in range(1,100):
        flag = False
        if i % 3 == 0:
            print("Fizz", end='')
            flag = True
        if i % 5 == 0:
            print("Buzz", end='')
            flag = True
        if not flag:
            print(i, end='')
        print(end=' ')
