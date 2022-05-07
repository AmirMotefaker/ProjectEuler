# Code by amotef@gmail.com

# projecteuler.net

# Circular primes
# Problem 35

# The number, 197, is called a circular prime because all rotations of the digits:
#                  197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


# Solution 1
# import time
# start_time = time.time()   #Time at the start of program execution

# def sieve(n):
# 	is_prime = [True]*n
# 	is_prime[0] = False
# 	is_prime[1] = False
# 	is_prime[2] = True
# 	for i in range(3,int(n**0.5+1),2):   	#even numbers except 2 have been eliminated
# 		index = i*2
# 		while index < n:
# 			is_prime[index] = False
# 			index = index+i
# 	prime = [2]
# 	for i in range(3,n,2):
# 		if is_prime[i]:
# 			prime.append(i)
# 	return prime

# primes = sieve(1000000)   #sieving prime numbers upto 1 million

# counter = 0  #counter to count the instances

# for i in primes:   #looping through prime numbers
# 	flag = True   	#assuming that there is no 2,4,6,8,5,0 in digits
# 	number = i/10  	#start with tens digit
# 	while number:   #looping through digits
# 		if (number%10) % 2 == 0 or (number%10)%5 == 0:
# 			flag = False
# 			break
# 		number //= 10
# 	if flag:   	#check if flag is true or false
# 		length = len(str(i))
# 		number = i
# 		counter += 1  #assume that the circular permutations are prime
# 		for j in range(length):	#loop to create circular permutations
# 			number = (number%10)*10**(length-1)+number//10
# 			if number not in primes: #if any permutation is not prime
# 				counter -= 1  #subtract one from counter
# 				break

# print ("Number of a Circular primes less than one million :", counter)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# While researching circular primes (not to be confused with permutable primes)
# it became clear that the only interesting ones are below one million. 
# After one million the only circular primes are repunits.

# Repunits are numbers composed of only 1s, and is described as R5 = 11111.
# Some of these circular-repunit primes include R19, R23, R317, R1031, R49081, and on from there.

# To solve this problem we generate a set of 78,498 prime numbers below 1 million using our prime_sieve() function.
# We remove all primes greater than five that contains any {0, 2, 4, 5, 6 or 8} which would make it non-prime during a rotation.
# That leaves only 1,113 prime candidates to investigate. They are added to the set primes along with 2 and 5.

import time
start_time = time.time()   #Time at the start of program execution

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def rotate(s):
    return [s[n:] + s[:n] for n in range(1, len(s))]

s = set('024568')
L = int(input("Enter a search limit less than 1,000,000? "))
primes = set(['2','5']+[p for p in map(str, prime_sieve(L)) if not set(p).intersection(s)])   # check numbers for primality
circular_primes = [int(p) for p in primes if all(pr in primes for pr in rotate(p))]   # the all() function returns True if all the rotations are a member of the primes set. 
                                                                                      # make p a circular prime number and it‘s added to the list.

print ("Number of circular primes below", L, " is",len(circular_primes))
print ("They are:", sorted(circular_primes), " With a sum of",sum(circular_primes))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
