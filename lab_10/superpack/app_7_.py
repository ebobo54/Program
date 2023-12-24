lst = [1,2,3,4,5]

def split(lst, n):
    return [lst[i::n] for i in range(n)]

print(split(lst, 3))
