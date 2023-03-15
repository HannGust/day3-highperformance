"""
Module containing the Person class definition
"""

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return " ".join((self.firstname, self.lastname))

    def printFullName(self):
        print(self.fullname())
