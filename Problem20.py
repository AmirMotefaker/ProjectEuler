# Code by amotef@gmail.com

# projecteuler.net

# Factorial digit sum
# Problem 20

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import time
start_time = time.time()   #Time at the start of program execution

def factorial(n):
	if n == 0:
		return(1)
	elif n == 1:
		return(1)
	else:
		return(n*factorial(n-1))

def main():
	x = 100
	answer = factorial(x)
	digits = list(str(answer))

	sum_of_digits = 0
	for digit in digits:
		sum_of_digits += int(digit)
	print(sum_of_digits)

main()

# print("100! =", factorial(100))
end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
