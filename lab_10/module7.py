# module7.py
def run_logic(arg1: int, arg2: str):
    print(f"Module 7: arg1={arg1}, arg2={arg2}")

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