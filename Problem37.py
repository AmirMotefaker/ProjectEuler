# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=37

# Truncatable primes
# Problem 37

# The number 3797 has an interesting property. Being prime itself, 
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

def check_if_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def check_if_truncatable(n):
    str_n = str(n)
    if not check_if_prime(int(str_n)):
        return False
    for i in range(1,len(str_n)):
        if not check_if_prime(int(str_n[i:])):
            return False
        if not check_if_prime(int(str_n[:-(i)])):
            return False
    return True


def main():
    list_of_truncatable_primes = []
    total = 0
    i = 10
    while len(list_of_truncatable_primes) < 11:
        if check_if_truncatable(i):
            list_of_truncatable_primes.append(i)
            total += i
        i += 1
    print(list_of_truncatable_primes)
    print("Sum of the only eleven primes are both truncatable =", total)


main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  748317
