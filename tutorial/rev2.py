#!/usr/bin/env python3

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for c in reverse('Golf'):
    print(c)


