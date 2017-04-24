#!/usr/bin/env python
# -*- coding: utf8 -*-

# 'ab' is short for 'a'ddress'b'ook

ab = { 'Swaroop'    : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
        }

print "Swaroop's address is", ab['Swaroop']

# deleteing a key-value pair
del ab['Spammer']

print '\nThere are {} contracts in the address-book\n'.format(len(ab))

for name, address in ab.items():
    print 'Contact {} at {}'.format(name, address)

# adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\nGuido's address is", ab['Guido']


