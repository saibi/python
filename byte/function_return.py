#!/usr/bin/env python
# -*- coding: utf8 -*-

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'equal'
    else:
        return y

print maximum(2, 3)

