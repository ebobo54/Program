# import typer
# from my_package import module7, module8, module9

# app = typer.Typer()

# @app.command()
# def run_module7(arg1: int, arg2: str):
#     module7.run_logic(arg1, arg2)

# @app.command()
# def run_module8(option1: bool = False):
#     module8.run_logic(option1)

# @app.command()
# def run_module9():
#     module9.run_logic()

# if __name__ == "__main__":
# # Запуск модуля7
# python main.py run_module7 --arg1 42 --arg2 "Hello"

# # Запуск модуля8
# python main.py run_module8 --option1

# # Запуск модуля9
# python main.py run_module9


# import typer

# from my_package import module7
# from my_package import module8
# from my_package import module9

# app = typer.Typer()


# @app.command()
# def foo(i: int):
#     print(f'i: {i}\n', module9.func(i))


# @app.command()
# def foo2(a: int, b: int):
#     print(f'a: {a}, b: {b}\n', module8.divide(a, b))

# @app.command()
# def foo3(lst: list, n: int):
#     print(f'lst: {lst}, n: {n}\n', module7.split(lst, n))

# if __name__ == "__main__":
#      app()


# python main.py foo 5
# python main.py foo2 10 2
# python main.py foo3

# import typer
# from typing import List

# from superpack import main2_8_
# from superpack import main_7_
# from superpack import app_7_

# app = typer.Typer()

# @app.command()
# def foo(i: int):
#     print(f'i: {i}\n', main_7_.func(i))

# @app.command()
# def foo2(a: int, b: int):
#     print(f'a: {a}, b: {b}\n', main2_8_.divide(a, b))

# @app.command()
# def foo3(lst: List[int], n: int):
#     print(f'lst: {lst}, n: {n}\n', app_7_.split(lst, n))

# if __name__ == "__main__":
#     app()

# main.py
from typing import Optional
import typer
from logic.intersection import intersect_with_duplicates, intersect_non_recursive
from logic.caching import cache_decorator
from logic.password_generator import password_generator

app = typer.Typer()

@app.command()
def run_intersection(
    list1: str = typer.Option(..., help="Comma-separated list of integers"),
    list2: str = typer.Option(..., help="Comma-separated list of integers"),
    use_recursive: bool = typer.Option(True, help="Use recursive method or not")
):
    list1 = list(map(int, list1.split(',')))
    list2 = list(map(int, list2.split(',')))

    if use_recursive:
        result = intersect_with_duplicates(list1, list2)
    else:
        result = intersect_non_recursive(list1, list2)

    print("Intersection Result:", result)

@app.command()
def run_caching():
    @cache_decorator
    def fibonacci_closure():
        a, b = 0, 1

        def generate_fibonacci():
            nonlocal a, b
            result = a
            a, b = b, a + b
            return result

        return generate_fibonacci

    fibonacci_gen = fibonacci_closure()

    for _ in range(10):
        print(fibonacci_gen())

@app.command()
def run_password_generator(
    number: int = typer.Option(..., help="Number of passwords to generate"),
    length: int = typer.Option(..., help="Length of each password"),
    num: int = typer.Option(..., help="Desired number of digits in each password"),
    special: int = typer.Option(..., help="Desired number of special characters in each password")
):
    for password in password_generator(number, length, num, special):
        print(password)

if __name__ == "__main__":
    app()


# python main.py run-password-generator --number 5 --length 12 --num 3 --special 2
# python main.py run-caching
# python main.py run-intersection --list1 "1,2,3,4" --list2 "2,3,4,6,8" --use-recursive
