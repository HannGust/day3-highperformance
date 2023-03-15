"""
Module containing the Student class definition, which inherits from the Person class
"""

from .person import Person

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject

    def printNameSubject(self):
        print(self.fullname() + ", " + self.subject)



class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course

    def printNameCourse(self):
        print(self.fullname() + ", " + self.course)
