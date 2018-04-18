#!/usr/bin/env python3

""" To take input of marks of a student of different subjects and tell if the student is passed """

n = int(input("Enter the number of students: "))
data = {}
languages = ('Physics', 'Maths', 'History')
for i in range(0,n):
    name = input("Enter the name of the student %d: " % (i + 1)) #Get the name of the student
    marks = []
    for x in languages:
        marks.append(int(input("Enter marks of %s: " % x))) #Get the marks for languages
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("%s 's total marks %d" % (x, total))
    if (total < 120):
        print("%s failed :(" % x)
    else:
        print("%s passed :)" % x)
