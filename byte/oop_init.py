#!/usr/bin/env python
# -*- coding: utf8 -*-

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print 'hello, my name is', self.name

p = Person('swaroop')
p.say_hi()

