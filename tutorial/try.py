#!/usr/bin/env python3


while True:
    try:
        x = int(input("Enter a number: "))
        break;
    except ValueError:
        print("Ooops! That was no valid number. try again...")


print('Number = ', x)

