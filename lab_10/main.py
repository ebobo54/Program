# main.py
import typer
from my_package import module7, module8, module9

app = typer.Typer()

# Здесь вы можете добавить аргументы и опции, которые будут передаваться в ваши модули

# Пример аргумента
@app.command()
def run_module7(arg1: int, arg2: str):
    module7.run_logic(arg1, arg2)

# Пример опции
@app.command()
def run_module8(option1: bool = False):
    module8.run_logic(option1)

# Запуск модуля 9 без аргументов
@app.command()
def run_module9():
    module9.run_logic()

if __name__ == "__main__":
    app()
