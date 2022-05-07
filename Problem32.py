# Code by amotef@gmail.com

# projecteuler.net

# Pandigital products
# Problem 32

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.



import time
start_time = time.time()   #Time at the start of program execution

products = set()   # store the products in a set to avoid duplicates

checked_later = set('123456789')   # Digits from 1-9 which will be checking later

for i in range(9):   # single digit multiplicand
	for j in range(999,9999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == checked_later:
			products.add(i*j)
		elif len(s) > 9:break

for i in range(9,99):   # double digit multiplicand
	for j in range(99,999):
		s = str(i)+str(j)+str(i*j)
		if len(s) == 9 and set(s) == checked_later:
			products.add(i*j)
		elif len(s)>9: break

print ("Sum of all Products as a 1 through 9 pandigital =", sum(products))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
