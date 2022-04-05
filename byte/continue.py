#!/usr/bin/env python
# -*- coding: utf8 -*-

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break;
    if len(s) < 3:
        print 'too small'
        continue
    print 'input is of sufficient length'



