# Code by amotef@gmail.com

# projecteuler.net

# Pandigital prime
# Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?


# Solution 1
# permutation method

# a = '123456789', which when permuted will give all the 1-9 pandigital numbers.
# If you don't want 1-9 pandigital and suppose say, you want only 1-7 pandigital number,
#  then consider only a[:7].

# flag = True

# j = 0, this one is while loop iterator

# While loop is executed because the value of flag is True at the instant.

# p = permutations(a[:9]) = permutations('123456789')

# As we know that the permutations will return all the numbers arranged from small to big.
# As we wanted bigger prime number we will check from last to first.
# I have used [::-1] to reverse the given list.

# Take an element from the permutations and then check if the last element is not even.

# Next condition uses the fact that all the prime numbers are of the form 6k+1 and 6k-1
# but the vice versa is not true.

# If the number passes the above test then check if it is prime.
# If it is prime then this will be the largest pandigital prime number because we are 
# coming in reverse order.

# If any prime is not found in the present iteration then start checking permutations 
# of '12345678', i.e.j = 8 = 9-1. At the end when the prime is found, 
# print the prime number and then flag = False to stop the outer while loop and break
# to stop the present for loop.

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
