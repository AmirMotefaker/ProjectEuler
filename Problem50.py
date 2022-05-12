# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=50

# Consecutive prime sum
# Problem 50

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time
start_time = time.time()   #Time at the start of program execution


def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):    # even numbers except 2 have been eliminated
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

primes = sieve(1000000)

length = 0   # length of the consecutive prime sum

largest = 0  # value of the consecutive prime sum

lastj = len(primes)   # max value of the j variable(second for loop)

for i in range(len(primes)):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

print (largest)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
