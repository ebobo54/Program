def nested_sqrt_recursive(n):
    if n == 3:
        return 3
    else:
        return (3 + nested_sqrt_recursive(n - 1)) ** 0.5
def nested_sqrt_non_recursive(n):
    result = 3
    for _ in range(n):
        result = (3 + result) ** 0.5
    return result
print(nested_sqrt_recursive(3))
print(nested_sqrt_non_recursive(3))
