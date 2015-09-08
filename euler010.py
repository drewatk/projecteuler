#!/usr/bin/env python

import math

def prime_sieve(n):
    
    primes = [True] * (n + 1)
    
    primes[0] = False
    primes[1] = False
    
    for i in range(2, n):
        if primes[i]:
            j = i * i
            while j < n + 1:
                primes[j] = False
                j += i
    
    result = []
    for i in range(len(primes)):
        if primes[i]:
            result.append(i)
            
    return result
    
primes = prime_sieve(2000000)

s = sum(primes)
print s
