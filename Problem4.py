# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=4

# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


import time
start_time = time.time()   #Time at the start of program execution    

def largestPalindromeProduct(n):
 
    upper_limit = (10**(n))-1  # largest number of n-1 digit. For example, for n = 2, upper_limit is 99
    lower_limit = 1 + upper_limit//10   # One plus this number is lower limit which is product of two numbers. For example, for n = 2, lower_limit is 10.
  
    max_product = 0 # Initialize result
    for i in range(upper_limit,lower_limit-1, -1):
     
        for j in range(i,lower_limit-1,-1): #  calculating product of two n-digit numbers
            product = i * j
            if (product < max_product):
                break
            number = product
            reverse = 0

            while (number != 0): # calculating reverse of product to check whether it is palindrome or not
                reverse = reverse * 10 + number % 10
                number =number // 10

            if (product == reverse and product > max_product):  # update new product if exist and if greater than previous one
                max_product = product

    return max_product
  
n1 = 2
n2 = 3
print('Largest palindrome product', n1, '- digit is: ', largestPalindromeProduct(n1))
print('Largest palindrome product', n2, '- digit is: ', largestPalindromeProduct(n2))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
