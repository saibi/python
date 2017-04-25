#!/usr/bin/env python
# -*- coding: utf8 -*-

import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')

pickle.dump(shoplist,f)
f.close()


print shoplist
del shoplist


f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)

print storedlist




