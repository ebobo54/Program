def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def limit_decorator(limit=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if limit is not None and result >= limit:
                raise StopIteration("Limit reached")
            return result

        return wrapper

    return decorator

fibonacci_gen = fibonacci_generator()

@limit_decorator(limit=100)
def fibonacci_with_limit():
    return next(fibonacci_gen)

for _ in range(15):
    try:
        print(fibonacci_with_limit())
    except StopIteration:
        print("Limit reached")
        break
