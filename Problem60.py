# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=60

# Prime pair sets
# Problem 60

# The primes 3, 7, 109, and 673, are quite remarkable. 
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


# Solution 1

# We will generate prime numbers upto 10000(Assumed) using Sieve of Erotosthenes. 

# Take the first number from the prime numbers list, let it be a
#   then take the second number the prime numbers list, let it be b . Remember that b > a.

# Check if ab & ba are primes, if they are primes, then take the third number from the 
#   prime numbers list, let it be c. Remember that c > b.

# Check if ac, ca, bc, ca are all primes. If they are primes then take a fourth number
#    from the prime numbers list, let it be d. Remember that d > c.

# Check if ad, da, bd, db, cd, dc are all primes. If they are all primes then take the
#    fifth number from the prime numbers list, let the number be e. Remember that e > d.  

# Now check if ae, ea, be, eb, ce, ec, de, ed are all primes. If they are all primes then find a + b + c + d + e.

# Now you might have got confused on why I am checking the primality of ab, ba, ac, ca .....


import time, random, math

start_time = time.time()   #Time at the start of program execution

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime


# Miller–Rabin primality test
# One of the best algorithm to check if the given number if prime
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Algorithm: http://bit.ly/2drtk0x
def is_prime(n, k = 3):
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n % 2 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d % 2 == 0:
         s, d = s + 1, d >> 1
      # A for loop with a random sample of numbers
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop


# A function to find all the combinations of the given two numbers
# and check if they are prime using the Rabin miller
def comb(a, b):
    len_a = math.floor(math.log10(a))+1
    len_b = math.floor(math.log10(b))+1
    if is_prime(int(a*(10**len_b)+b)) and is_prime(int(b*(10**len_a)+a)):
        return True
    return False


# finding out the primes upto 10000
primes = sieve(10000)

# problem solution
def prime_pairs():
    # a is first number
    for a in primes:
        # b is second number
        for b in primes:
            # check if b is less than a
            if b < a:
                continue
            # check if a and b satisfy the condition
            if comb(a, b):
                # c is the third number
                for c in primes:
                    # check if c is less than b
                    if c < b:
                        continue
                    # check if a,c and b, c satisfy the condition
                    if comb(a, c) and comb(b, c):
                        # d is the fourth number
                        for d in primes:
                            # check if d is less than c
                            if d < c:
                                continue
                            # check if (a,d), (b,d) and (c,d) satisfy the condition
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                # e is the fifth prime
                                for e in primes:
                                    # check if e is less than d
                                    if e < d:
                                        continue
                                    # check if (a, e), (b, e), (c, e) and (d, e) satisfy condition
                                    if comb(a, e) and comb(b, e) and comb(c, e) and comb(d, e):
                                        return a+b+c+d+e

# run the function and print the output
print (prime_pairs())

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   #Time of program execution
