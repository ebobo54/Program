def intersect_with_duplicates(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            list2.remove(item)
    return result

print(intersect_with_duplicates([1, 2, 3, 4], [2, 3, 4, 6, 8])) 
print(intersect_with_duplicates([5, 8, 2], [2, 9, 1]))            
print(intersect_with_duplicates([5, 8, 2], [7, 4]))  