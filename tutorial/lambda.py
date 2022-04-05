#!/usr/bin/env python3

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(18)

print(f(0))
print(f(2))


