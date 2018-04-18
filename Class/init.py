#!/usr/bin/env python3
class Student(object):
    """
    Returns a '''Student''' object with the given name, branch and year.
    
    """
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year
        print("A student object is created.")
    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
if __name__ == '__main__':
    name = input("Enter the name of the Student: ")
    branch = input("Enter the branch of the Student: ")
    year = input("Enter the year of the Student: ")
    std1 = Student(name, branch, year)
    std1.print_details()
