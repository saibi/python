#!/usr/bin/env python
# -*- coding: utf8 -*-

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'i have', len(shoplist), 'items to purchase.'

print 'these items are:' ,
for item in shoplist:
    print item,

print '\ni also have to buy rice.'
shoplist.append('rice')

print 'my shopping list is now', shoplist

print 'sort' 
shoplist.sort()
print shoplist

print 'first item', shoplist[0]

olditem = shoplist[0]
del shoplist[0]

print 'i bought the ', olditem

print 'my shopping list is now', shoplist

