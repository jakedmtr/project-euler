""" 
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the 
previous two terms. By starting with 1 and 2, the first 
10 terms will be:
    
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values 
do not exceed four million, find the sum of the even-valued terms.
"""

def sum_even_fibonacci(n):
    """ print all EVEN fibonacci numbers that are < n """
    a_n2 = 0 # if you want to start at 0 then set to -1
    a_n1 = 1
    counter = 0
    sum_a = 0
    while True:
        a_n = a_n2 + a_n1
        a_n2 = a_n1
        a_n1 = a_n
        if a_n >= n:
            break
        if a_n % 2 == 0:
            #print(a_n)
            sum_a += a_n
            counter += 1
        else:
            pass
    return sum_a

print(sum_even_fibonacci(4000000))