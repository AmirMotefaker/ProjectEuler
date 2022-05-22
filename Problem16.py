# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=16

# Power digit sum
# Problem 16

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

import time
start_time = time.time()   #Time at the start of program execution

def Power_digit_sum():  # Power digit sum
	total = 2**1000
	total = str(total)
	answer = 0
	for i in range(len(total)):
		answer += int(total[i])
	print("Power digit sum 2**1000 =",answer)
Power_digit_sum()

print("2**1000 =", 2**1000)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  1366
