#!/usr/bin/env python3

class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)


    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


r = Reverse("Hello")
for c in r:
    print(c)



