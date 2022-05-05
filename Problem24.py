# Code by amotef@gmail.com

# projecteuler.net

# Lexicographic permutations
# Problem 24

# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#                  012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Solution 1

# import time
# start_time = time.time()   #Time at the start of program execution

# import itertools
# def main():
# 	print(list(itertools.permutations(range(10)))[999999])

# main()

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

import time
start_time = time.time()   #Time at the start of program execution

from itertools import permutations  # import permutations from itertools

lexi_perm = list(permutations('0123456789'))  # lexi_perm: Lexicographic Permutations. converting the solution to a list(itertools.permutations)

solution = ', '.join(lexi_perm[999999])   # Each permutation is in the form of tuple so join all the strings to get solution

print (solution)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
