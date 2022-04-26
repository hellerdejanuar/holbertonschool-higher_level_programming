#!/usr/bin/env python3
def islower(c):
    ascii_ch = ord(c)
    if ascii_ch >= 97 and ascii_ch <= 122:
        return(True)
    else:
        return(False)
