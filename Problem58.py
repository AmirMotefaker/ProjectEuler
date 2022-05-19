# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=58

# Spiral primes
# Problem 58

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime;
# that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed. 
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


# Solution 1

# Step-by-Step
# Step 1: Write a function to test if the given number is prime.
# Step 2: Generate all the diagonal numbers in the spiral, 
#       For each and every new layer check if the ratio of length of prime numbers to the length of all numbers is less than 10%.
# Step 3: If the length is less than 10%, break the loop and print the square root of the last number.
#       Otherwise continue the next iteration with step1.

# import time
# start_time = time.time()   #Time at the start of program execution


# def is_prime(n):
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# i = 0

# gap = 1

# ratio = 1

# primes = []

# all_numbers = [1]

# while ratio > 0.1:
#     for j in range(4):
#         i += gap
#         present_number = 2*i + 1
#         all_numbers.append(present_number)
#         if is_prime(present_number):
#             primes.append(2*i + 1)
#     ratio = float(len(primes))/len(all_numbers)
#     gap += 1

# print ((2*i+1)**0.5)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   #Time of program execution



# Solution 2

import time
start_time = time.time()   #Time at the start of program execution

from sympy import isprime

def main():
    counter=0
    n=2
    while True:
        diagelements=[4*n*n-10*n+7,4*n*n-8*n+5,4*n*n-6*n+3,(2*n-1)**2]
        for x in diagelements:
            if isprime(x):
                counter+=1
                #print(x)
        #print(counter,4*n-3)
        if (counter/(4*n-3))<0.1:
            break
        n+=1
    print("The side length is: ",2*n-1)

if __name__ == '__main__':
    main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   #Time of program execution



#### Answer:  26241
