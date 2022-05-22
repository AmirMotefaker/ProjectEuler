# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=1

# Multiples of 3 or 5
# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
start_time = time.time()   #Time at the start of program execution

def multiple_3_or_5(n):
    if n % 3 ==0 or n % 5 ==0:
        return True
    else:
        return False

sum = 0
for i in range (1,1000):
    # print ("checking :" , i)
    if multiple_3_or_5(i):
        # print ("multiple is fine for", i)
        sum = sum + i
        # print ("Sum is =", sum)

print (sum)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  233168
