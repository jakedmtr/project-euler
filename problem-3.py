"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143?
"""

# find the the LARGEST prime factor of a number
""" the largest prime factor will just be the first prime factor that you
find if you start from the number itself """

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

def largestprimefactor(n):
    """ returns the largest prime factor of n """
    MAX_N = 1_000_000_000_000
    if n > MAX_N: # input limited so the program doesn't take forever
        print(f"You must enter a number less than {MAX_N}")
        return None
    else:
        test_num = 1 # variable init for both paths' while loops
        if n % 2 == 0: # even path
            while test_num <= n // 2:
                if n % test_num == 0:
                    if isprime(int(n/test_num)) == True:
                        print(f'{int(n/test_num)} [PRIME]')
                    else:
                        print(int(n/test_num))
                test_num += 1
        else: # odd path
            k = 0
            while test_num <= n // 2:
                test_num = 2*k + 1 # generate odd integer
                if n % test_num == 0 and isprime(int(n/test_num)) == True:
                    return int(n/test_num)
                k += 1
        print(1)

print(largestprimefactor(600851475143))