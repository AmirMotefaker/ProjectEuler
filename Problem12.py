# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=12

# Highly divisible triangular number
# Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#                   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?


import time, math
start_time = time.time()   #Time at the start of program execution

def count_factors(num):
    factors = 0
    for x in range(1,int(math.sqrt(num))+1):
        if num % x == 0:
            factors +=2
    return factors

seed = 1

searching = True

while searching: 
    seed += 1
    if seed % 2 == 0:
        factors = count_factors(seed/2)*count_factors(seed+1)
    else:
        factors = count_factors(seed)*count_factors((seed+1)/2)
    if factors > 500: break
        

print (int(seed*(seed+1)/2))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  76576500
