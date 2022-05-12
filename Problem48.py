# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=48

# Self powers
# Problem 48

# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

import time
start_time = time.time()   #Time at the start of program execution

solution = 0

for i in range(1, 1001):
    solution += i**i

print (str(solution)[-10:])   # printing the last 10 digits

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
