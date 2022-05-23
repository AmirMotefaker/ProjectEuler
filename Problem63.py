# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=63

# Powerful digit counts
# Problem 63

# The 5-digit number, 16807=75, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

from math import log10

s = 0
for n in range(1, 10):
    s += int(1 / (1 - log10(n)))

print ("n-digit integers that are an nth power =", s)

