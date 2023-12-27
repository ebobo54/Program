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
