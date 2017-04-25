#!/usr/bin/env python
# -*- coding: utf8 -*-

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = raw_input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print 'EOF'
except ShortInputException as ex:
    print ('ShortInputException: The input was ' + \
            '{0} long, expected at least {1}')\
            .format(ex.length, ex.atleast)
else:
    print 'end'

