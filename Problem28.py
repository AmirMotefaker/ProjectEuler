# Code by amotef@gmail.com

# projecteuler.net

# Number spiral diagonals
# Problem 28

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

#          21 22 23 24 25
#          20  7  8  9 10
#          19  6  1  2 11
#          18  5  4  3 12
#          17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


import time
start_time = time.time()   #Time at the start of program execution

def main():
	counter = 0
	gap_size = 1
	four_counter = 4
	total = 0
	for n in range(1, 1001**2 + 1):
		if counter == 0:
			total += n
			counter = gap_size
			four_counter -= 1
			#print('here', n)
		elif counter != 0:
			#print('here2', n)
			counter -= 1
		if four_counter == 0:
			gap_size += 2
			four_counter = 4
	print(total)
		# count 1, miss one (gap size), count, miss,... four counter, increase gap size

main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
