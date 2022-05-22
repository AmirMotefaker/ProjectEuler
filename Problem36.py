# Code by @AmirMotefaker

# projecteuler.net
# https://projecteuler.net/problem=36

# Double-base palindromes
# Problem 36

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)


# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

def palindrome_check(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] == str_n[-(i+1)]:
            continue
        else:
            return False
    return True


def convert_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    x = 1
    while x <= n:
        x *= 2
    x /= 2
    while x != 0.5:
        if x <= n:
            binary += '1'
            n -= int(x)
        else:
            binary += '0'
        x /= 2
    return binary


def main():
    total = 0
    for i in range(1_000_000):
        if palindrome_check(i):
            if palindrome_check(convert_to_binary(i)):
                total += i
    print(total)


main()

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution




# Solution 2

# import time
# start_time = time.time()   #Time at the start of program execution

# def compute():
# 	ans = sum(i for i in range(1000000) if is_decimal_binary_palindrome(i))
# 	return str(ans)


# def is_decimal_binary_palindrome(n):
# 	s = str(n)
# 	if s != s[ : : -1]:
# 		return False
# 	t = bin(n)[2 : ]
# 	return t == t[ : : -1]


# if __name__ == "__main__":
# 	print(compute())

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution



### Answer:  872187
