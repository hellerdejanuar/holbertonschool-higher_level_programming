#!/usr/bin/python3
def uppercase(str):

# iterate through letters in string
    for letter in str:
# if lowercase 
        ascii_ch = ord(letter)
        if ascii_ch >= 97 and ascii_ch <= 122:
            letter = chr(ascii_ch - 32)
        print(letter, end='')

    print()
