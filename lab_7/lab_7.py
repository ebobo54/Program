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
def intersect_with_duplicates(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            list2.remove(item)
    return result

print(intersect_with_duplicates([1, 2,2, 3, 4], [2, 3, 4, 2,6, 8])) 
print(intersect_with_duplicates([5, 8, 2], [2, 9, 1]))            
print(intersect_with_duplicates([5, 8, 2], [7, 4]))  
