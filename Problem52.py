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

import time
start_time = time.time()   #Time at the start of program execution

# while loop iterator
i = 1

# while loop
while True:
    if set(str(i)) == set(str(6*i)):
        if set(str(i)) == set(str(5*i)):
            if set(str(i)) == set(str(4*i)):
                if set(str(i)) == set(str(3*i)):
                    if set(str(i)) == set(str(2*i)):
                        print (i)
                        break
    i += 1

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
