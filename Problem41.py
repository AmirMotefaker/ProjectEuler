# Code by amotef@gmail.com

# projecteuler.net

# Pandigital prime
# Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


# Solution 1
# permutation method

from itertools import permutations  # permutations: Return successive r length permutations of elements in the iterable.
import time

start_time = time.time()   #Time at the start of program execution

def is_prime(n):  # check if the given number is prime or not.
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a = '123456789'  # starting with 1-9 digits

flag = True  # flag to stop while loop when prime is found

j = 9   # while loop iterator

while flag:
    p = permutations(a[:j])
    p = list(p)[::-1]
    for i in p:
        if int(i[j-1]) % 2 != 0:
            number = int(''.join(i))
            if (number+1) % 6 == 0 or (number-1) % 6 == 0:
                if is_prime(number):
                    print (number)
                    flag = False
                    break
    j -= 1

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
