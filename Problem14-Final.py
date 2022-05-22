# Code by lukegarbutt & @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=14

# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:

#            n → n/2 (n is even)
#            n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

#                13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#  Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


import time
def main():
    start_time = time.time()
    current_longest_chain = 0
    number_that_produced_chain = 0
    x = 1
    number_to_collatz_up_to = 1000000

    while (x < number_to_collatz_up_to):
        current_number = x
        current_chain = 1
        while (current_number != 1):
            current_number = collatz(current_number)
            current_chain += 1
        if current_chain > current_longest_chain:
            current_longest_chain = current_chain
            number_that_produced_chain = x
        #print(x, current_chain)
        current_chain = 1
        x += 1
    #print(number_that_produced_chain, current_longest_chain)
    print('The longest chain was {}, the number that produced this chain was {}, this took {} seconds to find.'.format (current_longest_chain, number_that_produced_chain, time.time() - start_time))



def collatz(number):
	if number % 2 == 0:
		number = number/2
	else:
		number = (number * 3) + 1
	number = int(number)
	return(number)
main()



### Answer:  837799
