"""
File: enhancedhistogram.py

Copyright (c) 2016 Lucas Blair

License: MIT

This program makes a chart of imput values with that number of asterisks following it.
""" 

numbers = []
response = " "

while (response == " "):
    numbers.append((int)(raw_input("Please enter a number!")))
    response = raw_input("Hit spacebar and enter to input another number. Hit only enter to print.")

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

print "n  |  Data"

largest_num = 0

for i in range(len(numbers)):
    if numbers[i] > largest_num:
        largest_num = numbers[i]

num_digits = digits(largest_num)
line_1 = "-"

j = 0

while j < num_digits:
    line_1 += "-"
    j += 1

line_1 += "+-----------------"
print line_1

def Histogram(number):
    asterisks = ""
    if digits(number) < num_digits:
        asterisks += " "
    asterisks += str(number)
    asterisks += " |  "
    for i in range(number):
        asterisks += "*"
    print asterisks




for i in range(len(numbers)):
    Histogram(numbers[i])
