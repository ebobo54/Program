# main.py
import typer
from my_package import module7, module8, module9

app = typer.Typer()

class ModuleRunner:
    def __init__(self, run_logic_func):
        self.run_logic_func = run_logic_func

    def run(self, **kwargs):
        self.run_logic_func(**kwargs)

@app.command()
def run_module7(arg1: int, arg2: str):
    runner = ModuleRunner(module7.run_logic)
    runner.run(arg1=arg1, arg2=arg2)

@app.command()
def run_module8(option1: bool = False):
    runner = ModuleRunner(module8.run_logic)
    runner.run(option1=option1)

@app.command()
def run_module9():
    runner = ModuleRunner(module9.run_logic)
    runner.run()

if __name__ == "__main__":
    app()



# python main.py run_module7 42 "hello"
# python main.py run_module8 --option1
# python main.py run_module9
