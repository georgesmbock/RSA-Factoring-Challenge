#!/usr/bin/python3
import sys
import time

"""n = 2
if len(sys.argv) == 1:
    print("Add argument")
    print("\tusage: python3 add.py file")
    exit()
"""
file = sys.argv[1]

f= open(file, "r")
    #line_str = f.readline()
for line_str in f:
    n = 2
    line_int = int(line_str)
    reste_modulo = (line_int % n)
    while reste_modulo == 0:
        r = line_int // n
    #if (line_int % n == 0):
        #r = line_int // n
        print(f"{line_int}={r}*{n}")
        break
            #n += 1
        #continue
    while reste_modulo != 0:
        n +=1
        if (line_int % n == 0):
            r = line_int // n
            print(f"{line_int}={r}*{n}")
            break
        #line_str = f.readline()
f.close()
