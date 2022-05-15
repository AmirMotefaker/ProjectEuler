# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=33

# Digit cancelling fractions
# Problem 33

# The fraction 49/98 is a curious fraction, 
# as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

# Numerator: the top number of a fraction
# Denominator: the bottom number of a fraction
# In a fraction, the denominator represents the number of equal parts in a whole, 
# and the numerator represents how many parts are being considered.

# Example:
# 16/64=1/4, 26/65=2/5, 19/95=1/5

# Solution 1
import time
start_time = time.time()   #Time at the start of program execution

d = 1
for i in range(1, 10):
    for j in range(1, i):
        q, r = divmod(9*j*i, 10*j-i)
        if not r and q <= 9:
            d*= i/float(j)

print ("Value of the denominator =", d)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution


# Solution 2
# import time
# start_time = time.time()   #Time at the start of program execution

# from fractions import Fraction

# product = 1   #Product of all the four fractions say 1 for now


# for i in range(10,100):   #'for' loops to generate Numerator and Denominator
# 	for j in range(i+1,100):
# 		common = list(set(str(i))&set(str(j)))   		#Intersection of Two sets(Common number between the two)
# 		if len(common) != 0:  	#Check if the list is not empty
# 			if common[0] != '0':   #Check if the common number is not 0
# 				num = list(str(i))
# 				den = list(str(j))
# 				num.remove(common[0])  	#Remove the common element from numerator
# 				den.remove(common[0]) 	#Remove the common element from Denominator
# 				if num[0]!='0' and den[0]!='0':   #Check if the value of num and den are not equal to 0
# 					if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):   #Check if they satisfy the question condition
# 						product *= Fraction(i,j)    #multiply to the product

# print ("Value of the denominator =", product.denominator)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  100
