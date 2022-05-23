# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=64

# Odd period square roots
# Problem 64


from math import sqrt

L, odd_period = 10000, 0

for N in range(2, L+1):
    r = limit = int(sqrt(N))
    if limit**2 == N: continue
    k, period = 1, 0
    while k !=1 or period == 0:
        k = (N - r * r) // k
        r = (limit + r) // k * k - r
        period += 1
    if period % 2 == 1: odd_period += 1

print ("Continuous deduction number for individual period =", odd_period)
