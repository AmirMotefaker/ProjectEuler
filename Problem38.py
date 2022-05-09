# Code by amotef@gmail.com

# projecteuler.net

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
