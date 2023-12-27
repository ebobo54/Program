# logic/caching.py
def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print(f"Cache hit for {func.__name__}{args}{kwargs}")
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        print(f"Cache miss for {func.__name__}{args}{kwargs}")

        return result

    return wrapper
