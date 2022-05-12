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


# Step 1: Make a list of prime numbers upto 1 million.

# Step 2: Create a variable to store length, consecutive prime sum and maximum value
# the second for loop iterator can take. Lets call them length, largest, lastj respectively.

# Step 3: Start a for loop(call this loop first for loop) and the maximum value 
# upto which it can loop will be upto the length of the prime numbers list generated in Step 1

# Step 4: Start another for loop(call this loop second for loop) nested in the 
# for loop of Step 3, and set the start value of the for loop as iterator value
# of first for loop added with the previous length of the largest consecutive prime sum.

# Step 5: Find the sum of the prime numbers after slicing the list with the 
# values of the iterator. Example: primes[i:j]

# Step 6: Check if the sum of the primes in of the sub list is less than 1 million. 
# If the value is less than 1 million then continue for Step 7, 
# otherwise change the value of the lastj to the value of j+1 and break the second for loop.

# Step 7: Check if the sum of the primes is a prime number and if it is a prime number,
# then change the value of length, to the length of the list generated in Step 5 and 
# the value of largest to the sum of the primes sub list.

# Step 8: Continue for the next iteration after this iteration is over.
# Finally print the value of largest to find the answer.

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
