# Code by amotef@gmail.com

# projecteuler.net
# https://projecteuler.net/problem=39

# Integer right triangles
# Problem 39

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


# The Pythagorean Theorem gives us: a**2 + b**2 = c**2 and by intuition a + b + c = p (perimeter).
# The decision to iterate perimeters has many advantages over generating right triangles.

# By iterating perimeters we need a method to check for integral (integer) right triangles.
# Since c = p–a–b, we can interpret the Pythagorean theorem as a**2 + b**2 = (p-a-b)**2
# After expanding and simplifying we have:
#        b = p(p-2a) / 2(p-a)
# By using a+b>c and symmetry we only need to investigate values of a to:
#           p / 2 + sqrt(2)

# Some other results:
# 10,000 = 9,240
# 100,000 = 55,440
# 1,000,000 = 720,720
# 10,000,000 = 6,126,120
# 100,000,000 = 77,597,520


# Solution 1

import time
start_time = time.time()   #Time at the start of program execution

L, t_max, p_max = 1000, 0, 0  #L must be an even integer

for p in range(L//4*2, L+1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_max: t_max, p_max = t, p
 
print ("Maximum perimeter, p <=",L,"is", p_max)
print ("Triangles in set =", t_max)

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution



# Solution 2

# import time
# start_time = time.time()   #Time at the start of program execution

# from collections import Counter   # Counter method

# perimeters = []   # list to store perimeters

# for a in range(1, 500):   # looping to generate a,b and c
#     for b in range(a, 500):
#         c = (a**2 + b**2)**0.5
#         if int(c) == c and a + b + c <= 1000:
#             perimeters.append(a+b+c)

# p = Counter(perimeters)   # counting the instances of perimeters

# print (p.most_common(1)[0])   # printing the most common perimeter or printing the most repeated perimeter

# end_time = time.time()   #Time at the end of execution
# print ("Time of program execution:", (end_time - start_time))   # Time of program execution
