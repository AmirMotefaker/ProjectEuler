# Code by amotef@gmail.com

# projecteuler.net

# Champernowne's constant
# Problem 40

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.12345678910-1-112131415161718192021...

# It can be seen that the 12**th digit of the fractional part is 1.

# If dn represents the n**th digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


# Solution 1

q = [9*(x+1) * pow(10, x) for x in range(20)]
def d(n):  # find the digit at position n in Champernowne's constant 
    i = 0
    while n>q[i]: n-= q[i]; i+= 1
    L, d = divmod((n-1), i+1)
    return int(str(pow(10, i)+L)[d])
n = input("Enter some indexes, separated by a space? ")
m = 1
for ci in map(int, n.split()):
    m*= d(ci)
print ("product =", m)
