#!/usr/bin/env python3

class Complex:
    """simle complex class"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.__doc__, x.r, x.i)
