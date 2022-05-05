# Code by amotef@gmail.com

# projecteuler.net
# Problem 6

# Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + .... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + 3 + .... + 10)**2 = 55*55 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
# 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Solution 1
# def sum_square_difference(n):
#       return (((n**2) * (n + 1)**2) / 4) - (n * (n + 1) * (2*n + 1) / 6)
# n = int(input("Enter Number: "))
# print(int(sum_square_difference(n)))


# Solution 2 

import time
start_time = time.time()   #Time at the start of program execution

def Square_difference(n):
 
    l = (n * (n + 1) * (2 * n + 1)) / 6  # sum of the squares of the first n natural numbers
    print("l = ", l)
     
    k = (n * (n + 1)) / 2   # sum of n naturals numbers
    print("k = ", k)
 
    k = k ** 2   # square of k
    print("k ** 2 = ", k)
     
    m = abs(l - k)    # Differences between l and k
    print("m = abs (l - k) = ", m)
     
    return m

x = int(input("Enter Number: ")) 
print("sum of the squares of the first", x,"natural numbers is", int(Square_difference(x)))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
