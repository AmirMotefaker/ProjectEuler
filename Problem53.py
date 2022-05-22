# Code by @AmirMotefaker

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

# import time
# start_time = time.time()   #Time at the start of program execution

# from math import factorial

# def choose(n, r):
# 	return factorial(n) / (factorial(r) * factorial (n-r))

# count = 0
# for n in range(1, 101):
# 	for r in range(1, n+1):
# 		if choose(n, r) > 1000000:
# 			count += 1

# print(count)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# Step 1:
# As you all know that two for loops required, one for n and one for r in nCr.
# According to the question the value of n(i.e first for loop) will start from 23 and end at 100. 
# Value of r is discussed in (2).

# Step 2:
# The value of r in nCr will be in range of 4, n-4 i.e 
# we can neglect the value of 0, 1, 2, 3, n-3, n-2, n-1, n. 

# import time
# start_time = time.time()   #Time at the start of program execution

# from math import factorial as f

# counter = 0

# def ncr(n, r):   # ncr: find the combinatorics
#     return f(n)/(f(r)*f(n-r))

# for n in range(23, 101):
#     for r in range(4, n-3):
#         if ncr(n, r) > 1000000:
#             counter += 1

# print (counter)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 3 - sympy
# The best way to solve this problem is to use the Pascal triangle:
# 	                            1	
#                           1		1	
#                       1		2		1	
#                   1		3		3		1	
#               1		4		6		4		1	
#           1		5		10		10		5		1	
#       1		6		15		20		15		6		1	
#   1		7		21		35		35		21		7		1

# Each row of this triangle is vertically symmetric,
# so C(n, r) = C(n, n-r) and any C(n, x) for x from r to (n-r) is greater than C(n, r).

# If C(n, r) > 106 then C(n, x) for x from r to (n-r) will also > 106,
# therefore, the number of C(n, r) > 106, is simply (n-r)-r+1 for that row n.

import time
start_time = time.time()   #Time at the start of program execution

from sympy import binomial
# SymPy is a Python library for symbolic mathematics.
# It aims to become a full-featured computer algebra system (CAS)
# while keeping the code as simple as possible in order to be comprehensible and easily extensible.

L, maxn, c = 1000000, 100, 0

for n in range(23, maxn + 1):
    for r in range(2, n//2):
        if binomial(n, r) > L:
            c+= n - 2*r + 1
            break

print ("Combinatoric selections =", c)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



#### Answer:  4075
