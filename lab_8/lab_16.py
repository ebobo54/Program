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
def add(a, b):
    print("Executing add function")
    return a + b

@cache_decorator
def multiply(x, y):
    print("Executing multiply function")
    return x * y


print(add(2, 3))  
print(add(2, 3))  

print(multiply(4, 5))  
print(multiply(4, 5))
