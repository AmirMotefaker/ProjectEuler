# Code by amotef@gmail.com

# projecteuler.net

# Digit factorials
# Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.


# Solution 1
# from math import factorial   #factorial function for calculating factorial

# import time
# start_time = time.time()   #Time at the start of program execution

# #factorials of numbers from 0-9
# f = [factorial(0),
# factorial(1),
# factorial(2),
# factorial(3),
# factorial(4),
# factorial(5),
# factorial(6),
# factorial(7),
# factorial(8),
# factorial(9)]

# def factorial_digits(n):   #sum of factorial of the digits
# 	s = 0
# 	while n:
# 		s += f[n%10]
# 		n //= 10
# 	return s

# solution = 0   #variable to save the value of solution

# for i in range(10,1854721):   #for loop to loop till 1854721
# 	if factorial_digits(i) == i:
# 		solution += i

# print (solution)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution


# Solution 2
import time
start_time = time.time()   #Time at the start of program execution

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


def main():
    final_total = 0
    for i in range(10, 100000):
        str_i = str(i)
        total = 0
        for digit in str_i:
            digit = int(digit)
            total += factorial(digit)
        if total == i:
            final_total += i
            print(i, final_total)


main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
