# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=3

# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29. Largest prime factor 13195 is 29.
# What is the largest prime factor of the number 600851475143 ?

# Prime Factor: any of the prime numbers that can be multiplied to give the original number.
# Example: The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).


import time
start_time = time.time()   #Time at the start of program execution

def FLPF(n): # FLPF: Find Largest Prime Factor
   PrimeFactor = 1 # A factor that is a prime number
   i = 2

   while i <= n / i:
      if n % i == 0:
         PrimeFactor = i
         n /= i
      else:
         i += 1

   if PrimeFactor < n: PrimeFactor = int(n)

   return PrimeFactor

print("Largest prime factor 100 is: ", FLPF(100))
print("Largest prime factor 13195 is: ", FLPF(13195))
print("Largest prime factor 600851475143 is: ", FLPF(600851475143))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution

# Find the prime factors of 100:
# 100 ÷ 2 = 50; save 2
# 50 ÷ 2 = 25; save 2
# 25 ÷ 2 = 12.5, not evenly so divide by next highest number, 3
# 25 ÷ 3 = 8.333, not evenly so divide by next highest number, 4
# But, 4 is a multiple of 2 so it has already been checked, so divide by next highest number, 5
# 25 ÷ 5 = 5; save 5
# 5 ÷ 5 = 1; save 5

# List the resulting prime factors as a sequence of multiples, 2 x 2 x 5 x 5 or as factors with exponents, 2**2 x 5**2.



### Answer:  6857
