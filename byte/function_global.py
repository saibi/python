#!/usr/bin/env python
# -*- coding: utf8 -*-

def func():
    global x

    print 'x is', x

    x = 2
    print 'changed global x to', x



x = 18
func()
print 'value of x is', x
