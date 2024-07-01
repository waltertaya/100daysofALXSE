from functools import lru_cache

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....

@lru_cache(maxsize=1000)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 0:
        raise ValueError('n must be a positive number')
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
