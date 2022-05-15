# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=41

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

# from itertools import permutations  # permutations: Return successive r length permutations of elements in the iterable.
# import time

# start_time = time.time()   #Time at the start of program execution


# def is_prime(n):  # check if the given number is prime or not.
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# a = '123456789'  # starting with 1-9 digits

# flag = True  # flag to stop while loop when prime is found

# j = 9   # while loop iterator

# while flag:
#     p = permutations(a[:j])
#     p = list(p)[::-1]
#     for i in p:
#         if int(i[j-1]) % 2 != 0:
#             number = int(''.join(i))
#             if (number+1) % 6 == 0 or (number-1) % 6 == 0:
#                 if is_prime(number):
#                     print (number)
#                     flag = False
#                     break
#     j -= 1

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2
# fastest algorithm

# A pandigital number doesn't needs to contain all numbers from 1 to 9,
# but all from 1 to length.
# try all permutations from 1 to 9 starting with 1 digit and going up,
# filtering all prime numbers and, then, taking largest one.

from itertools import permutations
import time

start_time = time.time()   #Time at the start of program execution


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# permutations of numbers from 1-7
p = permutations('1234567')

# for loop to loop from reverse order
# from higher to lower
for i in list(p)[::-1]:
    if int(i[6]) % 2 != 0:
        number = int(''.join(i))
        if (number+1) % 6 == 0 or (number-1) % 6 == 0:
            if is_prime(number):
                print (number)
                break

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution


# Solution 3

# This problem asks us to investigate the realm of pandigital numbers for the largest prime.
# An obvious question is: what is the value of n in n-digit pandigital prime? 
# We know it’s between 4 and 10 but that leaves a huge set of prime number candidates to search through.
# So let’s eliminate some values of n by using the divisibility rule which states that an integer is
# divisible by 3 whose sum of digits is divisible by 3 and therefore composite and not prime.

# # 9+8+7+6+5+4+3+2+1+0 = 45, 45/3 = 15
# 9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15
# 8+7+6+5+4+3+2+1 = 36, 36/3 = 12
# 7+6+5+4+3+2+1 = 28, 28/3 = 9.333…
# 6+5+4+3+2+1 = 21, 21/3 = 7
# 5+4+3+2+1 = 15, 15/3 = 5
# 4+3+2+1 = 10, 4/3 = 1.333…
# 3+2+1 = 6, 6/3 = 2
# 2+1 = 3 3/3 = 1

# Only pandigital numbers of length 4 and 7 can form a prime number. 
# The others cannot because any combination of their digits will sum to a number divisible by 3
# as affirmed by the commutative law of addition. So that leaves us to search odd 4 and 7 digit
# pandigital numbers for a prime number less than 4321 and 7654321 respectively.
# We also know that the candidate must end with a 1, 3, or 7 to be considered as a possible prime number,
# but this turned out to be of little consequence.
# Since we want the largest pandigital prime we’ll start with 7 digit numbers.

# def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

# import time
# start_time = time.time()   #Time at the start of program execution

# def is_prime(n):
#     if n <= 1: return False
#     if n <= 3: return True
#     if n%2==0 or n%3 == 0: return False
#     r = int(n**0.5)
#     f = 5
#     while f <= r:
#         if n%f == 0 or n%(f+2) == 0: return False
#         f+= 6
#     return True


# n = 7654321

# while not(is_pandigital(n, 7) and is_prime(n)): n-= 2

# print ("The largest existing n-digit pandigital prime is", n)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  7652413
