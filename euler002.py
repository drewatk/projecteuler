#!/usr/bin/env python

def fib_sequence(max):
    a = 0
    b = 1
    sequence = []
    
    while b < max:
        sequence.append(b)
        a, b = b, b + a
    
    return sequence
    
def find_evens(list):
    
    evens = []
    
    for n in list:
        if n % 2 == 0: evens.append(n)
        
    return evens
    
fib = find_evens(fib_sequence(4000000))
print sum(fib)
