# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=46

# Goldbach's other conjecture
# Problem 46

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


import math

import time
start_time = time.time()   #Time at the start of program execution


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True

number = 3

primes = [2]  # list of primes

while True:
    if is_prime(number):
        primes.append(number)
    else:
        for i in primes:
            if math.sqrt(((number-i)/2)) == int(math.sqrt(((number-i)/2))):
                break
        else:
            print (number)
            break

    number += 2

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
