#!/usr/bin/python3

def best_score(a_dictionary):
    best = [None, 0]
    if not a_dictionary:
        return None

    for key, value in a_dictionary.items():
        if value > best[1]:
            best = [key, value]

    return best[0]
