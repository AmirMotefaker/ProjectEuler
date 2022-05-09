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

# q = [9*(x+1) * pow(10, x) for x in range(20)]
# def d(n):  # find the digit at position n in Champernowne's constant 
#     i = 0
#     while n>q[i]: n-= q[i]; i+= 1
#     L, d = divmod((n-1), i+1)
#     return int(str(pow(10, i)+L)[d])
# n = input("Enter some indexes, separated by a space? ")
# m = 1
# for ci in map(int, n.split()):
#     m*= d(ci)
# print ("product =", m)



# Solution 2

# We have 9, 1 digit numbers
# 90, 2 digit numbers
# 900, 3 digit numbers
# 9000, 4 digit numbers
# 90000, 5 digit numbers
# 900000, 6 digit numbers

# Which will total to 5888889 digits. But we only need 1000000, so that
# 9 x 1 digit
# 90 x 2 digit
# 900 x 3 digit
# 9000 x 4 digit
# 90000 x 5 digit
# n x 6 digit

# = 9*1 + 90*2 + 900*3+ 9000*4 + 90000*5 + n*6 = 1000000
# So the value of n is approximately 85186 that means that we will have to do iterations until 185186.

import time
start_time = time.time()   #Time at the start of program execution

a = ''   # variable to store the values

for i in range(1, 185186):
    a += str(i)

d1 = int(a[0])

d10 = int(a[9])

d100 = int(a[99])

d1000 = int(a[999])

d10000 = int(a[9999])

d100000 = int(a[99999])

d1000000 = int(a[999999])

print (d1*d10*d100*d1000*d10000*d100000*d1000000)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
