# def fibonacci_closure():
#     a, b = 0, 1

#     def generate_fibonacci():
#         nonlocal a, b
#         while True:
#             yield a
#             a, b = b, a + b

#     generator = generate_fibonacci()
    
#     def fibonacci():
#         return next(generator)

#     return fibonacci

# fibonacci_gen = fibonacci_closure()

# for _ in range(10):
#     print(fibonacci_gen())

def fibonacci_closure():
    a, b = 0, 1

    def generate_fibonacci():
        nonlocal a, b
        while True:
            a, b = b, a + b
            return a

    return generate_fibonacci

fibonacci_gen = fibonacci_closure()

for _ in range(10):
    print(fibonacci_gen())
