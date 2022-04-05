#!/usr/bin/env python
# -*- coding: utf8 -*-

class SchoolMember:
    '''represents  any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'initialized schoolmember: {}'.format(self.name)

    def tell(self):
        '''tell my details.'''
        print 'name:"{}" age:"{}"'.format(self.name, self.age),

class Teacher(SchoolMember):
    '''represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'initialized teacher: {}'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'salary:"{}"'.format(self.salary)

class Student(SchoolMember):
    '''represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'initialized student: {}'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'marks:"{}"'.format(self.marks)

t = Teacher('mrs. shrividya', 40, 30000)

s = Student('swaroop', 25, 75)

# prints a blank line
print

members = [t, s]

for member in members:
    # works for both teachers and students
    member.tell()

