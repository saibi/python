#!/usr/bin/env python
# -*- coding: utf8 -*-

def print_max(x, y):
    """Prints the maximum of two numbers.

The two values must be integer."""
    # convert to integer if possible
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

print_max(1,10)

print print_max.__doc__
