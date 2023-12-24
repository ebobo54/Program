def A(func):
    def wrapper(*args, **kwargs): # внутри этой функции оборачиваем вызов исходной функции func в блок try-except
        try:
            return func(*args, **kwargs)
        except Exception as e:  # можно указать конкретные типы исключений
            print(f"Произошла ошибка: {e}")
    
    return wrapper

@A
def divide(a, b):
    result = a / b
    print(f"Результат деления: {result}")
