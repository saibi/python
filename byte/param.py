#!/usr/bin/env python
# -*- coding: utf8 -*-

def powersum(power, *args):
    '''return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print powersum(2, 3, 4)
print powersum(2, 10)

