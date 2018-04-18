#!/usr/bin/env python3
try:
    name = input("Enter a file name: ")
    fobj = open(name)
    res = 12 / 0
except ZeroDivisionError:
    print("We have an error in division.")
finally:
    fobj.close()
    print("Closing the file object.")
