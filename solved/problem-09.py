"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

a = 1
exit_status = 0  # for exiting while loop because i'm too stupid to figure out another way

while a < 997:
    if exit_status == 1:
        break
    for b in range(2, 998):
        c = sqrt((a**2)+(b**2))
        triplet = [a, b, c]
        if sqrt((a**2)+(b**2)) == (1000 - a - b):
            print(triplet[0] * triplet[1] * triplet[2])  # prints product from the 3 numbers in the triplet list
            exit_status = 1
            break
        b += 1
    a += 1
   

