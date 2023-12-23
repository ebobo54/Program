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

@cache_decorator
def fibonacci_closure():
    a, b = 0, 1

    def generate_fibonacci():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return generate_fibonacci

fibonacci_gen = fibonacci_closure()

for _ in range(10):
    print(fibonacci_gen())