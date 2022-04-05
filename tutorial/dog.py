#!/usr/bin/env python3

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind, d.name)
print(e.kind, e.name)

