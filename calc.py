import random

def rand_n(n_int: int) -> tuple:

    numbers = []
    for i in range(n_int):
        numbers.append(random.randint(-26, 13))

    sorted_numbers = sorted(numbers, reverse=True)

    negative_count = 0
    for num in numbers:
        if num < 0:
            negative_count += 1

    return negative_count, sorted_numbers
