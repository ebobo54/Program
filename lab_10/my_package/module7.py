from collections import Counter

def intersect_with_duplicates(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            list2.remove(item)
    return result

def intersect_non_recursive(list1, list2):
    result = []
    
    counter_list1 = Counter(list1)
    counter_list2 = Counter(list2)
    
    common_elements = counter_list1 & counter_list2

    for element, count in common_elements.items():
        result.extend([element] * count)

    return result

# Результаты для recursive
print(intersect_with_duplicates([1, 2, 3, 4], [2, 3, 4, 6, 8]))  
print(intersect_with_duplicates([5, 8, 2], [2, 9, 1]))          
print(intersect_with_duplicates([5, 8, 2], [7, 4]))              

# Результаты для non_recursive
print(intersect_non_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8])) 
print(intersect_non_recursive([5, 8, 2], [2, 9, 1]))            
print(intersect_non_recursive([5, 8, 2], [7, 4]))
