#!/usr/bin/env python3

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


x = Bag()

l = [1, 2, 3, 4]

x.addtwice(l)

print(x.data)
