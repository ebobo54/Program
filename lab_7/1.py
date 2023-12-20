def intersect_with_duplicates(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            list2.remove(item)
    return result

def nested_sqrt_recursive(n):
    if n == 1:
        return 3
    else:
        return (3 + nested_sqrt_recursive(n - 1)) ** 0.5

def nested_sqrt_non_recursive(n):
    result = 3
    for _ in range(n):
        result = (3 + result) ** 0.5
    return result

def combined_function(n):
    return nested_sqrt_recursive(n) ** 3, nested_sqrt_non_recursive(n) ** 3

print(intersect_with_duplicates([1, 2, 3, 4], [2, 3, 4, 6, 8]))
print(intersect_with_duplicates([5, 8, 2], [2, 9, 1]))
print(intersect_with_duplicates([5, 8, 2], [7, 4]))
print(combined_function(3))
