# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=49

# Prime permutations
# Problem 49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?


# Solution 1
# this Solution for n numbers

# import time
# start_time = time.time()   #Time at the start of program execution

# def all_primes_under(n):   # efficient by only checking primes under sqrt of number_to_check
#     assert n > 2
#     primes = [2]
#     number_to_check = 3
#     while number_to_check < n:
#         if not any([number_to_check%x == 0 for x in primes]):
#             primes.append(number_to_check)
#         number_to_check += 2
#     return primes

# def main():
#     primes = all_primes_under(10000)
#     primes_over_1000 = [i for i in primes if i >= 1000]
#     for prime in primes:
#         for gap in range(2, 4500, 2):
#             prime_2 = prime + gap
#             prime_3 = prime + (2 * gap)
#             if prime_2 in primes_over_1000 and prime_3 in primes_over_1000:
#                 if sorted(list(str(prime))) == sorted(list(str(prime_2))) == sorted(list(str(prime_3))):
#                     print(str(prime) + str(prime_2) + str(prime_3))

# if __name__ == '__main__':
#     main()

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution


# Solution 2

# step 1: Prime sieve upto 10000.
# step 2: Remove all the primes less than 1487 in the primes list 
#         which we have created in Step 1.
# step 3: Take each and every prime number and create permutations 
#         of the prime number.
# step 4: Remove all the duplicates in the list generated in Step 3.
#         Only unique elements are entertained.
# step 5: Sort the list in ascending order.
# step 6: If the length of the list generated till Step 5 is greater 
#         than or equal to 3 then go to Step 7 otherwise continue for next iteration.
# step 7: Start a for loop to iterate through each and every number in the list.
#         in the iteration, take a number and subtract it with other number, call it difference.
#         Now add the difference to the second element under consideration and check if the
#         new element(second number + difference) is in the list. If the new number is in the
#         list stop looping and return the three numbers, else continue with the next list.

from itertools import permutations
import time

start_time = time.time()   #Time at the start of program execution

def sieve(n):  # Sieve of Erotosthenes
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):       # even numbers except 2 have been eliminated
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


def create(b):   # create the number
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False

primes = sieve(10000)

primes = [x for x in primes if x > 1487]   # primes greater than 1487

for i in primes:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print (create(a))
            break

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
