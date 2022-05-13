# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=18

# Maximum path sum I
# Problem 18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)

# https://lucidmanager.org/data-science/project-euler-18/
# Project Euler 18 and 67 are identical, other than that the data in the second version is more extensive than in the first one.
# These two problems are logically similar to Project Euler 15.

import time
start_time = time.time()   #Time at the start of program execution

#numbers copied as string
number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

number = number.strip().split('\n')   #splitting the number into a list

for i in range(1,len(number)):   #converting each and every list of strings to int
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]

number[0] = [75]   #adding the first number bcz we could not do the above operation as this one one number

counter = 0   #counter for counting number of iterations


for i in range(len(number)-2,-1,-1):   #for loop for bottom-up approach
	for j in range(len(number[i])):
		number[i][j] = number[i][j] + max(number[i+1][j], number[i+1][j+1])
		counter += 1
	number.pop()

print ('Found {} in {} iterations'.format(number[0][0],counter))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
