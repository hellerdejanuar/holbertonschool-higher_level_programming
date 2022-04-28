#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    thisList = dir(hidden_4)

    for elem in thisList:
        if elem[:2] != "__":
            print(f"{elem}")
