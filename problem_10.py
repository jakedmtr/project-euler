"""
The sum of the primes below 10 is 2+3+5+7=17.
Find the sum of all the primes below two million.
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

print(sum(sieve(2_000_000)))

end = time.perf_counter()

print(f"Execution time: {end - start:.4f} seconds")