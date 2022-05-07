# Code by amotef@gmail.com

# projecteuler.net

# Circular primes
# Problem 35

# The number, 197, is called a circular prime because all rotations of the digits:
#                  197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


import time
start_time = time.time()   #Time at the start of program execution

def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	is_prime[2] = True
	for i in range(3,int(n**0.5+1),2):   	#even numbers except 2 have been eliminated
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = [2]
	for i in range(3,n,2):
		if is_prime[i]:
			prime.append(i)
	return prime

primes = sieve(1000000)   #sieving prime numbers upto 1 million

counter = 0  #counter to count the instances

for i in primes:   #looping through prime numbers
	flag = True   	#assuming that there is no 2,4,6,8,5,0 in digits
	number = i/10  	#start with tens digit
	while number:   #looping through digits
		if (number%10) % 2 == 0 or (number%10)%5 == 0:
			flag = False
			break
		number //= 10
	if flag:   	#check if flag is true or false
		length = len(str(i))
		number = i
		counter += 1  #assume that the circular permutations are prime
		for j in range(length):	#loop to create circular permutations
			number = (number%10)*10**(length-1)+number//10
			if number not in primes: #if any permutation is not prime
				counter -= 1  #subtract one from counter
				break

print ("Number of a Circular primes less than one million :", counter)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
