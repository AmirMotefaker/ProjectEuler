# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=55

# Lychrel numbers
# Problem 55

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers,
# like 196, never produce a palindrome. 
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
# Due to the theoretical nature of these numbers, and for the purpose of this problem,
# we shall assume that a number is Lychrel until proven otherwise. 
# In addition you are given that for every number below ten-thousand,
# it will either (i) become a palindrome in less than fifty iterations,
# or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
#  4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

# Solution 1

# Step-by-Step
# Step 1- check if the number is Lychrel number or not:
# - Start looping, and for each iteration check if sum of the number
#    and its reverse will form a palindrome or not. 
#    If the number is found to be a palindrome stop looping and return False.
# - If in the current iteration the value of the number is not found to be a palindrome
#    then change the number to the sum of the number and its reverse and continue iterations.
# Step 2 :
# Loop through all the numbers from 0 to 10000 and for each number 
# check if it is Lychrel number using the function created in Step 1. 
# If the number is Lychrel then increase the counter by 1.

import time
start_time = time.time()   #Time at the start of program execution


def is_lychrel(n):   #check is lychrel number or not
    for i in range(50):      #fifty iterations
        number = n + int(str(n)[::-1])  #sum of number and reverse
        if str(number) == str(number)[::-1]:   #check palindrome
            return False
        n = number
    return True

counter = 0

for i in range(10001):
    if is_lychrel(i):
        counter += 1

print (counter)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   #Time of program execution
