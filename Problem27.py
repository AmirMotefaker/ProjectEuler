# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=27

# Quadratic primes
# Problem 27

# Euler discovered the remarkable quadratic formula:
#                n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
# However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
#  n² + an + b, where |a| < 1000 and |b| < 1000


# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.


# this link is very useful:
# https://radiusofcircle.blogspot.com/2016/04/problem-27-project-euler-solution-with-python.html

import time
start_time = time.time()   #Time at the start of program execution

def Sieve_of_Eratosthenes(n):   # Sieve of Eratosthenes: problem 7 solution
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def is_prime(n):   # number	is prime or not
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

primes1000 = Sieve_of_Eratosthenes(1000)   # primes below 1000

primes = primes1000[:]   # copy of primes1000 variable

largest_value = 0   # assume the largest value is 0 at start


for b in primes1000:   # quadratic equation
	for a in primes1000:
		i = 0
		while True:   #positive a and b
			quadratic = i**2+a*i+b
			if quadratic not in primes:
				if is_prime(quadratic):
					primes.append(quadratic)
				else:
					if i-1 > largest_value:
						largest_value = i-1
						axb = a*b
					break
			i += 1
		i = 0
		while True:   		#negative a and positive b
			quadratic = i**2-a*i+b
			if quadratic not in primes:
				if is_prime(quadratic) and quadratic>0:
					primes.append(quadratic)
				else:
					if i-1 > largest_value:
						largest_value = i-1
						axb = -1*a*b
					break
			i += 1

print (axb)   #largest value of a*b

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  -59231
