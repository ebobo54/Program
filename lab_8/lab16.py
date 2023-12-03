from functools import lru_cache

def cache_decorator(maxsize=None):
    def decorator(func):
        if maxsize is None:
            cached_func = lru_cache()(func)
        else:
            cached_func = lru_cache(maxsize)(func)

        def wrapper(*args, **kwargs):
            return cached_func(*args, **kwargs)

        return wrapper

    return decorator

@cache_decorator(maxsize=128)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@cache_decorator() 
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(5)) 
print(factorial(5))   

print(fibonacci(7))   
print(fibonacci(7))   
