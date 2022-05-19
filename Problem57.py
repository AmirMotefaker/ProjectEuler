# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=57

# Square root convergents
# Problem 57

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
# 
# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408,
# but the eighth expansion, 1393/985, is the first example where the number of 
# digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions,
# how many fractions contain a numerator with more digits than denominator?


# This link is very useful:
# https://mathworld.wolfram.com/Convergent.html

# Solution 1
# if p/q is is the first convergent then the next convergent can be written as (p+2q)/(p+q).

# import time
# start_time = time.time()   #Time at the start of program execution

# p = 1
# q = 1

# counter = 0

# for i in range(1000):
#     a1 = p + 2*q
#     b1 = p + q
#     if len(str(a1)) > len(str(b1)):
#         counter += 1
#     p = a1
#     q = b1

# print (counter)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   #Time of program execution



# Solution 2
# Expand the series as 2d + n for the numerator and d+n for the
# denominator and count the number of times the length of the 
# numerator exceeds the denominator as strings.

# Using base 10 logs for the number of digits comparison between
# the numerator and denominator yields a 100 times speed improvement
# over comparing the lengths of them converted to strings.

import time
start_time = time.time()   #Time at the start of program execution

from math import log10
L, n, d, c = 1000, 3, 2, 0

for x in range(2, L+1):
    n, d = n + 2*d, n + d
    if int(log10(n)) > int(log10(d)): c += 1

print ("Numerator more digits than denominator =", c)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   #Time of program execution



#### Answer:  153
