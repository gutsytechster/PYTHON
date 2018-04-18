#!/usr/bin/env python3
name = input("Enter the file name: ")
with open(name) as fobj:
    for line in fobj:
        print (line)
