# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=31

# Coin sums
# Problem 31

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#                  1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#                  1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?


import time
start_time = time.time()   #Time at the start of program execution

target_Pound = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target_Pound

for coin in coins:
    for i in range(coin, target_Pound+1):
        ways[i] += ways[i-coin]

print ("How many different ways to make £2 =", ways[target_Pound])

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
