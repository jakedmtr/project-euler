""" The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
        (1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is
        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum. """ 
import time

start = time.perf_counter()

print((sum(range(1,101))**2)-sum(n**2 for n in range(1,101)))

end = time.perf_counter()

print(f"Execution time: {end - start:.10f} seconds")