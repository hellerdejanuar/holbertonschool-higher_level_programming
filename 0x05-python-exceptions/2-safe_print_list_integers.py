#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cn = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cn += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print()
            raise
            return cn
    print()
    return cn
