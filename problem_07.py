""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time

start = time.perf_counter()

# We will create a function which implements the sieve of eratosthenes
def sieve(target):
    # Assume every number is prime initially
    is_prime = [True] * (target + 1)

    # 0 and 1 are not prime
    is_prime[0] = False
    is_prime[1] = False

    # Only need to sieve up to sqrt(target)
    for p in range(2, int(target ** 0.5) + 1):

        # If p hasn't been eliminated, it is prime
        if is_prime[p]:

            # Eliminate multiples of p, starting from p²
            for multiple in range(p ** 2, target + 1, p):
                is_prime[multiple] = False

    # The indexes still marked True are the primes
    primes = [i for i, prime in enumerate(is_prime) if prime]

    return primes

# start the sieve with a limit of 100,000
limit = 100_000
primes = sieve(limit)

# keep perfoming sieve until length of primes list is 10,000.
# the 10,000th item in list is the 10,001st prime.
while True:
    primes = sieve (limit)
    if len(primes) > 10000:
        print(primes[10000])
        break
    limit += 1000

end = time.perf_counter()

print(f"Execution time: {end - start:.6f} seconds")