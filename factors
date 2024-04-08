#!/usr/bin/python3

import sys
import time

file = sys.argv[1]

f = open(file, "r")
for line_str in f:
    n = 2
    line_int = int(line_str)
    reste_modulo = line_int % n
    while reste_modulo == 0:
        r = line_int // n
        print(f"{line_int}={r}*{n}")
        break
    while reste_modulo != 0:
        n += 1
        if (line_int % n == 0):
            r = line_int // n
            print(f"{line_int}={r}*{n}")
            break
f.close()
