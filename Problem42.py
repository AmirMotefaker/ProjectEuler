# Code by amotef@gmail.com

# projecteuler.net

# Coded triangle numbers
# Problem 42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#              1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position
# and adding these values we form a word value. For example,
# the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

# Solution 1
# from math import sqrt

# import time
# start_time = time.time()   #Time at the start of program execution

# score = lambda word: sum(ord(c)-ord('A')+1 for c in word)
# is_tn = lambda t: (sqrt(1 + 8*t) - 1) / 2 % 1 == 0
# print ("Number of triangle words =", 
#     sum(is_tn(score(x[1:-1])) for x in open('Problem42_words.txt').read().split(',')))

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2
import string
import csv
import math

import time
start_time = time.time()   #Time at the start of program execution


def main():
    letter_to_number_dict = dict(zip(string.ascii_uppercase, [ord(c) % 32 for c in string.ascii_uppercase]))
    with open('Problem42_words.txt', 'r') as f:
        reader = csv.reader(f)
        words = list(reader)[0]
    total = 0
    for word in words:
        score = 0
        for letter in word:
            score += letter_to_number_dict[letter]
        if is_square(8*score+1):
            total += 1
    print(total)


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
