# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=38

# Pandigital multiples
# Problem 38

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
# concatenated product of an integer with (1,2, ... , n) where n > 1?


# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

def check_if_pandigital(n):
    str_n = str(n)
    if len(str_n) != 9:
        return False
    for i in range(1,10):
        if str(i) not in str_n:
            return False
    return True

def concatonate_products(n):
    x = 2
    result = str(n)
    while len(result) < 9:
        result += str(n*x)
        x += 1
    return result

def main():
    answers = []
    for i in range(100_000):
        concat = concatonate_products(i)
        if check_if_pandigital(concat):
            print(i, concat)
            answers.append(concat)
    print(max(answers))

main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# For example, take the number 327, Now we will start multiplying it with 1
# 327 x 1 = 327
# 327 x 2 = 654
# 327 x 3 = 981
# Now the concatenated product is 327654981, whose length is 9 digits so stop iteration and proceed for next decision.

# For example, 7932
# 7932 x 1 = 7932
# 7932 x 2 = 15864
# Concatenated product is 793215864 which has 9 digits and so we can stop here. 

# this link is useful
# https://radiusofcircle.blogspot.com/2016/05/problem-38-project-euler-solution-with-python.html


# import time
# start_time = time.time()   #Time at the start of program execution

# # largest pandigital number
# largest = 0

# # for loop to loop till 4 digits
# for i in range(1,10000):
	
# 	# value for concatenated product
# 	multiplication = ''
	
# 	# (1,2,3,4,.....n)
# 	integer = 1
	
# 	# if the multiplication < 9 digits
# 	while len(multiplication) < 9:
		
# 		# concatenating the product at each stage
# 		multiplication += str(i*integer)
		
# 		# incrementing (1,2,3,4,....n)
# 		integer += 1
		
# 	# check for digits less than 9
# 	# check for all 1-9 numbers
# 	# check if '0' not in concatenated sting
# 	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) 
# 		and ('0' not in multiplication)):
	
# 		# check if multiplication is greater than largest
# 		if int(multiplication) > largest:
# 			largest = int(multiplication)

# # printing the largest
# print (largest)

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  932718654
