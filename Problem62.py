# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=62

# Cubic permutations
# Problem 62


# The cube, 41063625 (3453), can be permuted to produce two
# other cubes: 56623104 (3843) and 66430125 (4053). In fact,
# 41063625 is the smallest cube which has exactly three 
# permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.


from itertools import permutations
import time

# time at the start of program
start = time.time()



# first list
list_1 = [1, 2, 3]

# second list
list_2 = [3, 2, 1]

# check if both the lists are same
print (list_1 == list_2)

print ("First List")
# lets print the permutations of first list
for i in permutations(list_1):
    print (i)

print ("Second List")
# lets print the permutations of second list
for j in permutations(list_2):
    print (j)



# list to store cubes
cubes = []

# iterator
i = 0

# while loop
while True:
 # cube of the number
 cube = sorted(list(str(i**3)))
 # appending the cube to cubes list
 cubes.append(cube)
 # check if it occured 5 times
 if cubes.count(cube) == 5:
  # print the cube of the smallest such cube
  print ((cubes.index(cube))**3)
  break
 i += 1




# i
i = 27

# str(i**3)
print (str(i**3))

# list(str(i**3))
print (list(str(i**3)))

# sorted(list(str(i**3)))
print (sorted(list(str(i**3))))


# time at the end of program
end = time.time()

# total time taken
print (end - start)
