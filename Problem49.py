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

import time
start_time = time.time()   #Time at the start of program execution

def all_primes_under(n):   # efficient by only checking primes under sqrt of number_to_check
    assert n > 2
    primes = [2]
    number_to_check = 3
    while number_to_check < n:
        if not any([number_to_check%x == 0 for x in primes]):
            primes.append(number_to_check)
        number_to_check += 2
    return primes

def main():
    primes = all_primes_under(10000)
    primes_over_1000 = [i for i in primes if i >= 1000]
    for prime in primes:
        for gap in range(2, 4500, 2):
            prime_2 = prime + gap
            prime_3 = prime + (2 * gap)
            if prime_2 in primes_over_1000 and prime_3 in primes_over_1000:
                if sorted(list(str(prime))) == sorted(list(str(prime_2))) == sorted(list(str(prime_3))):
                    print(str(prime) + str(prime_2) + str(prime_3))

if __name__ == '__main__':
    main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
