#!/usr/bin/env python
# -*- coding: utf8 -*-

print 'simple assignment'

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

mylist = shoplist[:]
del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist


