# Code by amotef@gmail.com

# projecteuler.net

# Lattice paths
# Problem 15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


# Binomial coefficient function
# The binomial coefficient (nCk) is the number of ways of picking k unordered outcomes from n possibilities,
#  also known as a combination or combinatorial number. The symbols nCk are used to denote a binomial coefficient,
#  and are sometimes read as "n choose k."
# (nCk)={(n!)/(k!(n-k)!)   for 0<=k<n
#  0   otherwise

# https://mathworld.wolfram.com/BinomialCoefficient.html


from math import factorial

import time
start_time = time.time()   #Time at the start of program execution

def BCF(n,k):   # BCF:Binomial coefficient function
	return factorial(n)/(factorial(k)*factorial(n-k))
print ('Number of lattice paths is: '+str(BCF(20+20,20)))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
