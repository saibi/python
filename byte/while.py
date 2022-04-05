#!/usr/bin/env python
# -*- coding: utf8 -*-

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'you guessed it'
        running = False

    elif guess < number:
        print 'higher than that'
    else :
        print 'lower than that'

else:
    print 'The while loop is over'

print 'done'

