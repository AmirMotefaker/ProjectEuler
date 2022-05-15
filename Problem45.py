# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=45

# Triangular, pentagonal, and hexagonal
# Problem 45

# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	  Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	  Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	  Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.


# Solution 1

import time
start_time = time.time()   #Time at the start of program execution


def is_pentagonal(p):   # is_pentagonal check if the given number is pentagonal
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


def is_hexagonal(h):   # is_hexagonal check if the given number is hexagonal
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False

i = 286  # iterator start after 285

while True:   # loop for iterating
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print (triangle)
        break
    i += 1

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# import time
# start_time = time.time()   #Time at the start of program execution

# def generate_triangle_number(n):
#     return(n*(n+1)/2)


# def generate_pentagonal_number(n):
#     return n*((3*n)-1)/2


# def generate_hexagonal_number(n):
#     return n*(2*n-1)


# def main():
#     triangle_numbers = [1]
#     pentagonal_numbers = [1]
#     triangle_n = 2
#     pentagonal_n = 2
#     hexagonal_n = 2
#     while True:
#         hexagonal_number = generate_hexagonal_number(hexagonal_n)
#         hexagonal_n += 1
#         while hexagonal_number > triangle_numbers[-1]:
#             triangle_numbers.append(generate_triangle_number(triangle_n))
#             triangle_n += 1
#         while hexagonal_number > pentagonal_numbers[-1]:
#             pentagonal_numbers.append(generate_pentagonal_number(pentagonal_n))
#             pentagonal_n += 1
#         if hexagonal_number in triangle_numbers and hexagonal_number in pentagonal_numbers:
#             print(hexagonal_number)


# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution

# main()



### Answer:  1533776805
