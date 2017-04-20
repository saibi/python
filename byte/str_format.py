#!/usr/bin/env python
# -*- coding: utf8 -*-

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format(name))
print('{name} wrote {book}'.format(name='Kim', book = 'byte book'))
print('{name} wrote {book}'.format(name=name, book = 'apple'))

print 'no newline',
print 'hohoho'
