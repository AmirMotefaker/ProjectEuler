# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=65

# Convergents of e
# Problem 65

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

nx, ny = 1, 2
L = int(input("Numerator of Nth convergent, N="))
for i in range(2, L+1): 
    ny, nx = (1 if i%3 else 2*i//3)*ny + nx, ny

print (sum(map(int, str(ny))), ny)
