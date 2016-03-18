"""
File: smoothedheaiside.py

Copyright (c) 2016 Lucas Blair

License: MIT

Prints the result of the corresponding equation for a inputed value of x.
""" 

from math import pi
from math import sin



def H_eps(x, eps = 0.01):
    if x < -eps:
        result = 0
    elif x <= eps:
        result = 0.5 * (1 + (x/eps) + sin(pi*((x/eps)/pi)))
    else:
        result = 1
    return result

def test_H_eps():
    x_str = raw_input ("Enter the value of x:")
    x = float(x_str)
    print H_eps(x)

test_H_eps()
