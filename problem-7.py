""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def isprime(N):
    """ returns true if n is prime """
    """ if answer isnt instant then N is most likely prime. program
    is extremely quick at finding if a number is NOT prime for odd N 
    that are """
    i = 1
    divisors_count = 0

    while i < N:
        if divisors_count > 1:
            break
        if N % 2 == 0 or N % 5 == 0:
            divisors_count += 1
            break
        if N == 0:
            break
        divisor = 2*i + 1
        if divisor > N // 2:
            break
        if N % divisor != 0:
            i += 1
        else:
            divisors_count += 1
            #print(f'{N} divided by {divisor} is {N/divisor}')
            break

    if divisors_count == 1 and N == 2:
        return True
    elif divisors_count == 1 and N == 5:
        return True
    elif divisors_count == 0 and N != 1 and N != 0:
        return True
    else:
        return False

counter = 0
n = 1
nth_prime = 0
while counter < 10001:
    if isprime(n):
        counter += 1
    if counter == 10001:
        nth_prime = n
    n += 1
print(nth_prime)