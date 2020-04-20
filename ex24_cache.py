import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(2,50):
    print('{} --- {}'.format(i, fib(i)))
stop = time.time()

print(stop-start)


