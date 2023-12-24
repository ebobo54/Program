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

import typer
from typing import List

from superpack import main2_8_
from superpack import main_7_
from superpack import app_7_

app = typer.Typer()

@app.command()
def foo(i: int):
    print(f'i: {i}\n', main_7_.func(i))

@app.command()
def foo2(a: int, b: int):
    print(f'a: {a}, b: {b}\n', main2_8_.divide(a, b))

@app.command()
def foo3(lst: List[int], n: int):
    print(f'lst: {lst}, n: {n}\n', app_7_.split(lst, n))

if __name__ == "__main__":
    app()
