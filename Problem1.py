# Code by @AmirMotefaker
# https://codereview.stackexchange.com/questions/276758/project-euler-problem-1-multiples-of-3-or-5-python

# projecteuler.net
# Problem 1

# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Solution 1
import time
start_time = time.time()   #Time at the start of program execution

def multiple_3_or_5(n):
    if n % 3 ==0 or n % 5 ==0:
        return True
    else:
        return False

sum = 0
for i in range (1,1000):
    # print ("checking :" , i)
    if multiple_3_or_5(i):
        # print ("multiple is fine for", i)
        sum = sum + i
        # print ("Sum is =", sum)

print (sum)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2 - Best
# https://codereview.stackexchange.com/questions/276758/project-euler-problem-1-multiples-of-3-or-5-python


def main():
    TESTS = (
        (10, 23),
        (1000, 233168),
    )
    for limit, expected in TESTS:
        got = euler_1(limit)
        if got == expected:
            print('ok')
        else:
            print(limit, got, expected)

def euler_1(limit = 1000):
    return sum(i for i in range (1, limit) if multiple_3_or_5(i))

def multiple_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0

if __name__ == '__main__':
    main()
    
    #### Answer:  233168

