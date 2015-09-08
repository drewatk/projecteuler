#!/usr/bin/env python

def sumSquares(n) :
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum
    
def sumNumbers(n) :
    sum = 0
    for i in range(1, n + 1):
        sum += i 
    return sum       
n = 100
squaresum = sumSquares(n)
numbersum = sumNumbers(n)
print squaresum
print numbersum
print (numbersum ** 2) - squaresum
