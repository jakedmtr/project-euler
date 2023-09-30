""" 2520 is the smallest number that can be divided by each of the 
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20? """

numbers = []

for i in range(1,21):
    numbers.append(i)

numbers.reverse()

n = numbers[0]

while n != numbers[-1]:  # get rid of the numbers that are already factors of larger numbers so we don't waste time
    for i in reversed(numbers):
        if n == i:
            pass
        elif n % i == 0:
            numbers.remove(i)
    n -= 1

counter = 19
step = 19
success_count_goal = len(numbers)
success_count = 0

while success_count != success_count_goal:
    for num in numbers:
        if counter % 2 != 0 and str(num)[-1] != '0':
            success_count = 0
            break
        if counter % num == 0:
            print(f"{counter} is divisible by {num}")
            success_count += 1
        else:
            print(f"{counter} is NOT divisible by {num}")
            success_count = 0
            step = num
            break
    counter += step

