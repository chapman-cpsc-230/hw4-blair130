"""
File: count_pairs.py

Copyright (c) 2016 Lucas

License: MIT

this program counts the number of pairs of AT in a DNA sequence.
""" 

n_str = raw_input("Enter the DNA sequence:")

def count_pairs(DNA, pair):
    cnt = 0
    num_pairs = 0
    while cnt < (len(DNA) - 1):
        if DNA[cnt] == pair[0] and DNA[cnt + 1] == pair[1]:
            num_pairs += 1
        cnt += 1
    print num_pairs

count_pairs(n_str, "AT")
