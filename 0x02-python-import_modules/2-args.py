#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    plural = '' if argc == 2 else 's'
    term = '.' if argc == 1 else ':'

    print(f"{argc - 1} argument{plural}{term}")

    if argc > 1:
        for i in range(argc):
            print(f"{i}: {argv[i]}")
