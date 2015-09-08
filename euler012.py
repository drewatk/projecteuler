#!/usr/bin/env python
import math

#returns the nth triangle number
def triangle_number(n):
	return sum(range(n + 1))

#returns number of factors of n
def find_factors(n): 
	
	factors = 0
	
	for i in range(1, int(round(math.sqrt(n)+1))):
		if not n % i : factors += 2

	return factors

target_factors = 500
i = 0
n = 0

while n < target_factors:
	i += 1
	t = triangle_number(i)
	n = find_factors(t)
	

print 'Result:' 
print i
print t
print n