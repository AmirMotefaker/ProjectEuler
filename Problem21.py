# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=21

# Amicable numbers
# Problem 21

# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are
# an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

# https://oeis.org/A259180
# Amicable pairs:
# 220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856,
# 12285, 14595, 17296, 18416, 63020, 76084, 66928, 66992, 67095, 71145, 
# 69615, 87633, 79750, 88730, 100485, 124155, 122265, 139815, 122368, 
# 123152, 141664, 153176, 142310, 168730, 171856, 176336, 176272, 180848, 
# 185368, 203432, 196724, 202444, 280540, 365084

#        Amicable    pair           Sum

#             x        y           x + y

#   ------------------------------------

#    n    A002025   A002046       A180164

#   ------------------------------------

#    1       220      284           504

#    2      1184     1210          2394

#    3      2620     2924          5544
 
#    4      5020     5564         10584

#    5      6232     6368         12600

#    6     10744    10856         21600

#    7     12285    14595         26880

#    8     17296    18416         35712

#    9     63020    76084         139104

#   10     66928    66992         133920

#   11     67095    71145         138240

#   12     69615    87633         157248
 

import time
start_time = time.time()   #Time at the start of program execution

# We begin by initializing a list, ds[], to all ones,
# L elements long and fill it by sieving the sum of proper divisors.
# The primary i loop only needs to reach the square root of our limit,
# L (11000 in this case – enough to find the next pair outside our limit of 10000).
from math import sqrt
L = 130000; ds = [1]*L
for i in range(2, int(sqrt(L))):
    for j in range(i+1, L//i):
        ds[i*j]+= i+j

# Then, filter from the list, ds[], amicable pairs by appending ds[i] and i to the list an[].
# Remember, for numbers to qualify as amicable pairs they must meet the criteria d(d(a)) = a, where d(a) < a.
an = []
for i in range(2, L):
    if ds[i] < i and ds[ds[i]] == i: an+= [ds[i], i]

# Finally, sum amicable numbers from the list an[] that are less than N. 
# Keep mindful of a reasonable search limit for the depth of sums of proper divisors long since rehearsed.
N = int(input("Limit? "))
print ("Amicable sum less than",N,"=", sum(a for a in an if a<N))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  31626
