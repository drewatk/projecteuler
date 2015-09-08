#!/usr/bin/env python

# Project Euler problem 14: Longest Collatz Sequence

def collatz(n, count = 1):
	
	if n == 1: 
		return count

	if not n % 2:
		return collatz(n / 2, count + 1)
	else:
		return collatz(3 * n + 1, count + 1)

def find_largest_collatz(max):
	
	largest = (0, 0)

	for i in range(1, max + 1):
		
		c = collatz(i)
		if c > largest[0]:
			largest = (c, i)

	return largest

print find_largest_collatz(1000000)