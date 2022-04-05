#!/usr/bin/env python
# -*- coding: utf8 -*-

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def alpha_only(text):
    for c in text:
        if not c.isalpha():
            text = text.replace(c, '')

    return text

    

something = raw_input("Enter text: ")

a = alpha_only(something)
if is_palindrome(a):
    print 'yes, it is a palindrome', a
else:
    print 'no, it is not a palindrome'
