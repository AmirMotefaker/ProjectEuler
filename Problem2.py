# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=2

# Even Fibonacci numbers
# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

def IsEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

first = 1
second = 2

sum = 0

while (first < 4000000):
    # print ("my first number is", first)
    if IsEven(first):
        # print ("oh it is even")
        sum = sum + first
        # print ("-----------> now the sum is", sum)
    new = first + second
    first = second
    second = new
print(sum)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# import time
# start_time = time.time()   #Time at the start of program execution

# a, b = 1, 1
# total = 0
# while a <= 4000000:
#     if a % 2 == 0:
#         total += a
#     a, b = b, a+b  # the real formula for Fibonacci sequence
# print (total)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution


### Answer:  4613732
