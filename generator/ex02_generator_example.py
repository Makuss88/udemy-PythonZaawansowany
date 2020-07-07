import random


def get_new_tasty(numbers_of_value: int, asserted_sum: int):
    counter = 0
    taste = list(range(numbers_of_value))

    while True:
        counter += 1

        for i in range(numbers_of_value):
            taste[i] = random.randint(1, 101)

        if sum(taste) == asserted_sum:
            yield counter, taste
            counter = 0


for i in range(10):
    (count, number) = next(get_new_tasty(3, 100))
    print(count, number)
