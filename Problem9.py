# Code by amotef@gmail.com

# projecteuler.net
# Problem 9

# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import time
start_time = time.time()   #Time at the start of program execution

for a in range(3, 1000):
    for b in range (a + 1, 999):
        c_Square = a**2 + b**2
        c = c_Square**0.5

        if a + b + c == 1000:
            product = a * b * c
            sum_a_b_c = a + b + c
            print("a =", a)
            print("b =", b)
            print("c =", int(c))
            print(a,"+",b,"+",int(c), "=", int(sum_a_b_c))
            print("Product of a,b,c(a*b*c) =",int(product))
            break

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
