#!/usr/bin/env python3

#Multiplication of two matrices
n = int(input("Enter the value of n: "))
print("Enter the values for Matrix A")
a = []
for i in range(0,n):
    a.append([int(x) for x in input("").split(" ")])
print("Enter the values for Matrix B")
b = []
for i in range(0,n):
    b.append([int(x) for x in input("").split(" ")])
c = []
for i in range(0,n):
    c.append([sum([a[i][k] * b[k][j] for k in range(0,n)]) for j in range(0,n)])
print("After matrix multiiplication")
print("-" * 10 * n)
for x in c:
    for y in x:
        print("%5d" % y, end = ' ')
    print("")
print("-" * 10 * n)
