# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=22

# Names scores
# Problem 22

# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?


import time
start_time = time.time()   #Time at the start of program execution

def main():
	with open("p022_names.txt") as file:
		names_file = file
		names_list = []
		for i in names_file:
			names_list.append(i)
	
	new_list = names_list[0].split(',')
	sorted_list = sorted(new_list)
	sum_of_scores = 0
	counter = 1
	for i in sorted_list:
		sum_of_scores += counter * score_name(i)
		counter += 1
	print(sum_of_scores)

def score_name(name):
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	score = 0
	for i in name:
		counter = 1
		for j in alphabet:
			if j == i:
				score += counter
			else:
				counter += 1
	return(score)




main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  871198282
