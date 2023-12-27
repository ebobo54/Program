# logic/intersection.py
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
