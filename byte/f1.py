#!/usr/bin/env python
# -*- coding: utf8 -*-


def func(x):
    print 'x is', x

    x = 2

    print 'changed local x to', x


x = 18
func(x)
print ' x is still', x


