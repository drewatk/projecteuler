#!/usr/bin/env python

def bruteForce():
    
    a = 0
    b = 0
    c = 0
    
    sum = 1000
    found = False

    for a in range(1, sum):
        for b in range(1, sum):
            c = sum - a - b

            if (a ** 2) + (b ** 2) == (c ** 2) :
                found = True
                break

        if found: break

    return [a, b, c]

answers = bruteForce()
print answers
