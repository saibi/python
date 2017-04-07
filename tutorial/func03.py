#!/usr/bin/env python3

def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(voltage=100)
parrot(voltage=18, action='VOOOOOOM')
parrot(action='VOOM', voltage=38)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

