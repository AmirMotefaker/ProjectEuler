# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=23

# Non-abundant sums
# Problem 23


# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.



# Solution 1

# import time

# start_time = time.time()   #Time at the start of program execution

# def main():
# 	dict_of_numbers = {}
# 	list_of_abundant_numbers = []
# 	for i in range(1, 28124):
# 		dict_of_numbers[i] = i
# 	for i in dict_of_numbers:
# 		if i < sum(factorise(i)):
# 			list_of_abundant_numbers.append(i)

# 	print('factoring done')

# 	for number_1 in list_of_abundant_numbers:
# 		for number_2 in list_of_abundant_numbers:
# 			total = number_1 + number_2
# 			if total in dict_of_numbers:
# 				dict_of_numbers.pop(total)
# 	print(dict_of_numbers)
# 	print(sum(dict_of_numbers))

# def factorise(number):
# 	factors = []
# 	x = 1
# 	while(x < number):
# 		if number % x == 0:
# 			factors.append(x)
# 		x += 1
# 	return(factors)

# start_time = time.time()
# main()
# print(time.time()-start_time)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

import time


from math import sqrt   

start = time.time()

def divisors(n):   # generate divisors of given number, Example: divisors(28) will give [1,2,4,7,14]
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n/i])
	return list(set(divs))


ab = []   # store the values of abundant numbers

for i in range(12,28123):   # generate the abundant numbers
	if sum(divisors(i))>i:
		ab.append(i)


non_ab_sum = [x for x in range(28123)]   # assume all the numbers are not sum of abundant numbers 

for i in range(len(ab)):   # generate sum of two abundant numbers
	for j in range(i,28123):
		if ab[i]+ab[j] < 28123:
			non_ab_sum[ab[i]+ab[j]] = 0   # value of the abundant sum (negating)
		else:
			break

print (sum(non_ab_sum))   # value of the sum of non abundant sum
        
print (time.time() -start)   # total execution time



### Answer:  4179871
