#!/usr/bin/env python3

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []
        print("init")

    def f(self):
        return 'hello world'


x = MyClass()

print(x.__doc__)

x.counter = 1
while  x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
del x.counter
print(x.counter)

