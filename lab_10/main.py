import typer

from my_package import module7
from my_package import module8
from my_package import module9

app = typer.Typer()


@app.command()
def foo(i: int):
    print(f'i: {i}\n', module9.func(i))


@app.command()
def foo2(a: int, b: int):
    print(f'a: {a}, b: {b}\n', module8.divide(a, b))

@app.command()
def foo3(lst: list, n: int):
    print(f'lst: {lst}, n: {n}\n', module7.split(lst, n))

if __name__ == "__main__":
     app()


# # Запуск модуля7
# python main.py run_module7 --arg1 42 --arg2 "Hello"

# # Запуск модуля8
# python main.py run_module8 --option1

# # Запуск модуля9
# python main.py run_module9
