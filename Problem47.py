# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=47

# Distinct primes factors
# Problem 47

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each.
#  What is the first of these numbers?


# We have created npf function an abbreviation for Number of Prime Factors.
# This function will return the number of prime factors. 
# npf follows the traditional Factor Tree method with a little modification.
# Usually with the factor tree method we will have to loop till the end of the number is reached. 
# But one can find that there is only one prime factor after the square root of the given number. 
# So we will simplify our looping till the square root of the number and add 1 to the final solution.

# j = 2*3*5*7
# We are starting with this number because, this is the minimum number that can be formed.

import time
start_time = time.time()   #Time at the start of program execution


def npf(number):
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

j = 2*3*5*7   # iterator

while True:
    if npf(j) == 4:
        j += 1
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    print (j-3)
                    break
    j += 1

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
