# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=56

# Powerful digit sum
# Problem 56

# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a**b, where a, b < 100, 
# what is the maximum digital sum?


# Solution 1
# Step 1: find the sum of digits of the given number. The function is as follows:
#   -Let the number be n.
#   -Start a while loop. Create a variable to store the sum of numbers.
#   -Find the remainder of the number when divided by 10.
#    This remainder will be the last digit. Add this number to the sum.
#   -Divide the number with 10 and go again for step 2, until the number becomes 0.
# Step 2: Create two for loops both in the range of 0 to 100.
#    One for a and one for b. Now find if any of the previous values of sum of digits
#    is lesser than the present one, then assign the present value to the largest.
#    In a similar way continue till the end of the loop.

# import time
# start_time = time.time()   #Time at the start of program execution


# def sum_of_digits(n):   #sum of digits of given number
#     sod = 0
#     while n != 0:
#         sod += n % 10
#         n //= 10
#     return sod

# largest = 0

# for a in range(0, 100):
#     for b in range(0, 100):
#         sod = sum_of_digits(a**b)
#         if sod > largest:
#             largest = sod

# print (largest)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   #Time of program execution



# Solution 2 - fastest algorithm

import time
start_time = time.time()   #Time at the start of program execution

print ("Maximum digital sum =",)
print (max(sum(map(int, str(a**b))) for a in range(60, 100) for b in range(80, 100)))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   #Time of program execution
