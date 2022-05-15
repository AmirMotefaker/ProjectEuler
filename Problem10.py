# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=10

# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time
start_time = time.time()   #Time at the start of program execution

def is_Prime(n):
    if n < 2: return "It is not a prime number."
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 0
for i in range(2, 2000000):
    if is_Prime(i):
        sum += i

print ("Sum of all the primes below two million =", sum)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  142913828922
