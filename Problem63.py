# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=63

# Powerful digit counts
# Problem 63

# The 5-digit number, 16807=75, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

# Solution 1

# from math import log10

# s = 0
# for n in range(1, 10):
#     s += int(1 / (1 - log10(n)))

# print ("n-digit integers that are an nth power =", s)



# Solution 2

# counter = 0

# # for loop to loop from 1 to 9
# for i in range(1, 10):
#     power = 1
#     while True:
#         if power == len(str(i ** power)):
#             counter += 1
#         else:
#             break
#         power += 1

# # print the number of instances found
# print (counter)



# Solution 3

def compute():
	ans = sum(1
		for i in range(1, 10)
		for j in range(1, 22)
		if len(str(i**j)) == j)
	return str(ans)


if __name__ == "__main__":
	print(compute())
