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

def fibonacci_closure():
    a, b = 0, 1

    def generate_fibonacci():
        nonlocal a, b
        a, b = b, a + b
        return a

    return generate_fibonacci

fibonacci_gen = cache_decorator(fibonacci_closure())  # Применяем декоратор к generate_fibonacci

def add(a, b):
    print("Executing add function")
    return a + b + fibonacci_gen()

def multiply(x, y):
    print("Executing multiply function")
    return x * y + fibonacci_gen()

# Вызываем функции
print(add(2, 3))
print(add(2, 3))
print(multiply(4, 5))
print(multiply(4, 5))

fibonacci_gen = fibonacci_closure()
for _ in range(10):
    print(fibonacci_gen())