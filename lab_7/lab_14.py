# def nested_sqrt_recursive(n):
#     if n == 1:
#         return 3
#     else:
#         return (3 + nested_sqrt_recursive(n - 1)) ** 0.5

# def nested_sqrt_non_recursive(n):
#     result = 3
#     for _ in range(n - 1):
#         result = (3 + result) ** 0.5
#     return result

# print(nested_sqrt_recursive(1))
# print(nested_sqrt_non_recursive(1))

def nested_sqrt_recursive(n):
    if n == 1:
        return 3**0.5
    else:
        return (3 + nested_sqrt_recursive(n - 1)) ** 0.5

def nested_sqrt_non_recursive(n):
    result = 3**0.5
    for _ in range(n - 1):
        result = (3 + result) ** 0.5
    return result

print(nested_sqrt_recursive(3))
print(nested_sqrt_non_recursive(3))
