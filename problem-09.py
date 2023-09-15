"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
c^2 = a^2 + b^2
c = sqrt(a^2 + b^2)
a = sqrt(c^2 - b^2)
b = sqrt(c^2 - a^2)

a + b + c = 1000 = sqrt(c^2 - b^2) + sqrt(c^2 - a^2) + sqrt(a^2 + b^2)
"""

impossible