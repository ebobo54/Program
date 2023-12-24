def func(i):
    if i == 1:
        print(0)
        return 0
    elif i == 2:
        print(0)
        return 0
    elif i == 3:
        print(1.5)
        return 1.5
    else:
        A = (i+1)/((i*i)+1) * func(i-1) - func(i-2) * func(i-3)
        print(A)
        return A


# func()