#!/usr/bin/env python

n = 1
target = 10001
primes = []
while len(primes) < target:
    n += 1   
    for d in primes:
        if n % d == 0: 
            break
    else:
        print n, 'is a prime number'
        primes.append(n)

