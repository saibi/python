#!/usr/bin/env python3

knights = {'gallahad': 'the pure', 'robin' : 'the brave'}

for k, v in knights.items():
    print(k, v)


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

print(zip(questions, answers))



for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

