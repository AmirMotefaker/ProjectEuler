# Code by amotef@gmail.com

# projecteuler.net

# 1000-digit Fibonacci number
# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:
#        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Solution 1

# def fibonacci(a, b, n):
#     if n == 1:
#         return a
#     else: 
#         return fibonacci(a+b, a, n-1)


# print (fibonacci(1, 0, 12))



# Solution 2
# loop instead of recursion

# def fibonacci(n):
#     a = 1
#     b = 0
#     while n > 1:
#         a, b = a+b, a
#         n = n - 1
#     return a

# print (fibonacci(12))



# Solution 3

import time
start_time = time.time()   #Time at the start of program execution

term = 2
fib = [1, 1]
while len(str(fib[1])) < 1000:
    term += 1
    fib = [fib[1], fib[0] + fib[1]]

print (term)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
