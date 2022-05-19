# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=52

# Permuted multiples
# Problem 52

# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


# Solution 1
# This problem is straight forward and there is no big algorithm that I have used.
# I have used a series of if statements to get the solution.
# The only thing I want to mention is that, we will start with checking if all the
# digits of the multiple of 6(i*6) are present in the given number(i).
# Then 5(i*5), 4(i*4), 3(i*3), 2(i*2). 
# Using 6 will reduce the number of iterations and thus reduces the execution time.

# import time
# start_time = time.time()   #Time at the start of program execution

# # while loop iterator
# i = 1

# # while loop
# while True:
#     if set(str(i)) == set(str(6*i)):
#         if set(str(i)) == set(str(5*i)):
#             if set(str(i)) == set(str(4*i)):
#                 if set(str(i)) == set(str(3*i)):
#                     if set(str(i)) == set(str(2*i)):
#                         print (i)
#                         break
#     i += 1

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2 - fastest 
# This is repeating digits:

# 1/7 = 0.142857 142857 142857 ...
# 2/7 = 0.285714 285714 285714 ...
# 3/7 = 0.428571 428571 428571 ...
# 4/7 = 0.571428 571428 571428 ...
# 5/7 = 0.714285 714285 714285 ...
# 6/7 = 0.857142 857142 857142 ...

# I’m sure you get the idea without giving away the answer.

# As for our programmatic solution: an assumption that the 
# digits didn’t have to be unique, I set the number of digits
# less one as our starting bound and search sequentially by 
# sorting the digits within each number and comparing for multiples 1, 2, 3, 4, 5 and 6.

# We can begin our search with a 5 digit multiple of 9, such as 99999, 
# because the result has at least 6 digits.
# Also, because any number and its permutation always differ by a multiple of 9
# (ex., (45121-11542)/9 = 3731) we can increment by 9 instead of 1.

import time
start_time = time.time()   #Time at the start of program execution

f = lambda n:sorted(str(n))

n = 99999
while not f(n*2) == f(n*3) == f(n*4) == f(n*5) == f(n*6): n += 9

print ("Permuted multiples(smallest positive integer) =", n)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
