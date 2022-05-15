# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=30

# Digit fifth powers
# Problem 30

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


import time
start_time = time.time()   #Time at the start of program execution

solution = 0  # sum be 0 at the start

for i in range(2,5*9**5+1):   # 5(10-1)^5
	if sum([int(x)**5 for x in str(i)]) == i:
		solution += i

print (solution)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  443839
