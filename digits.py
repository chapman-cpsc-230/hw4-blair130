"""
File: digits.py

Copyright (c) 2016 Lucas Blair

License: MIT

This program tells how many digits are in a number including negative signs.
""" 

n_str = raw_input ("Enter a natural number:")
n = int(n_str)

def digits(n):
    cnt = 0
    if n < 0:
        cnt += 1
        n = -n
    while n > 0:
        n /= 10
        cnt += 1
    return cnt
    cnt = 1

for j in range(1):
    print digits(n)
