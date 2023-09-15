""" 2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20? """

def mindivby1to20():
    """ returns the smallest number < n that is divisible by 1-20 """
    num1 = 20
    num2 = 11
    dontneed = [3]
    need = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    goodnumbers = []
    while num1 <= 999999999:
        if len(goodnumbers) == 1:
            return goodnumbers[0]
        divisors = []
        while num2 <= 20:
            if num2 in dontneed:
                break
            if num1 % num2 == 0:
                divisors.append(num2)
            else:
                break
            num2 += 1
        num2 = 11
        if divisors == need:
                goodnumbers.append(num1)
        num1 += 20
    return "Range too small"