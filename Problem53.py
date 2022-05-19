# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=53

# Combinatoric selections
# Problem 53

# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.
# In general, nCr = n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×…×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

from math import factorial

def choose(n, r):
	return factorial(n) / (factorial(r) * factorial (n-r))

count = 0
for n in range(1, 101):
	for r in range(1, n+1):
		if choose(n, r) > 1000000:
			count += 1

print(count)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
