#!/usr/bin/env python3
lst = [1, 2, 3, 4, 5]
def square(num):
    "Returns the square of a given number."
    return num * num
print(list(map(square, lst)))
