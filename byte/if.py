#!/usr/bin/env python
# -*- coding: utf8 -*-


number = 23

guess = int(raw_input('Enter an integer: '))

if guess == number:
    # new block starts here
    print('Congraturations, you guessed it.')
elif guess < number:
    print('no it is a little highter that that')
else:
    print('no it is a little lower than that')

print('done')


