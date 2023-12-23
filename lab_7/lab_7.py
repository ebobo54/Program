# def intersect_recursive(list1, list2):
#     if not list1 or not list2:
#         return []

#     head = list1[0]
#     tail = list1[1:]

#     if head in list2:
#         return [head] + intersect_recursive(tail, list2)
#     else:
#         return intersect_recursive(tail, list2)
# def intersect_non_recursive(list1, list2):
#     return list(set(list1) & set(list2))
# print(intersect_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8]))  
# print(intersect_recursive([5, 8, 2], [2, 9, 1]))          
# print(intersect_recursive([5, 8, 2], [7, 4]))               

# print(intersect_non_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8])) 
# print(intersect_non_recursive([5, 8, 2], [2, 9, 1]))            
# print(intersect_non_recursive([5, 8, 2], [7, 4]))     

# def intersect_with_duplicates(list1, list2):
#     result = []
#     for item in list1:
#         if item in list2:
#             result.append(item)
#             list2.remove(item)
#     return result

# print(intersect_with_duplicates([1, 2,2, 3, 4], [2, 3, 4, 2,6, 8])) 
# print(intersect_with_duplicates([5, 8, 2], [2, 9, 1]))            
# print(intersect_with_duplicates([5, 8, 2], [7, 4]))  

# from collections import Counter

# def intersect_recursive(list1, list2):
#     if not list1 or not list2:
#         return []
    
#     head, *tail = list1
#     if head in list2:
#         list2.remove(head)
#         return [head] + intersect_recursive(tail, list2)
#     else:
#         return intersect_recursive(tail, list2)

# def intersect_non_recursive(list1, list2):
#     result = []
#     counter_list1 = Counter(list1)
#     counter_list2 = Counter(list2)
    
#     for item in (counter_list1 & counter_list2).elements():
#         result.extend([item] * min(counter_list1[item], counter_list2[item]))

#     return result

# # Результаты для intersect_recursive
# print(intersect_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8]))  
# print(intersect_recursive([5, 8, 2], [2, 9, 1]))          
# print(intersect_recursive([5, 8, 2], [7, 4]))              

# # Результаты для intersect_non_recursive
# print(intersect_non_recursive([1, 2, 3, 4], [2, 3, 4, 6, 8])) 
# print(intersect_non_recursive([5, 8, 2], [2, 9, 1]))            
# print(intersect_non_recursive([5, 8, 2], [7, 4]))


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
