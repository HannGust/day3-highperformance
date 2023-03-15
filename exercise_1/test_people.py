"""
Test of the people package, with the classes Person, Student and Teacher classes.
"""

import people

per1 = people.Person("Per", "Persson")
per1.printFullName()


stud1 = people.Student("Winston", "Thursson", "Social Sciences")
#stud1.printFullName()
stud1.printNameSubject()


teach1 = people.Teacher("Humpry", "Davy", "Chemistry II")
#teach1.printFullName()
teach1.printNameCourse()

