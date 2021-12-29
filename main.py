
# Modules

import os
import math
from rich.console import Console
from loguru import logger as log
from time import sleep
from random import randint as rand

# Default Variebles

console = Console()

# Logic

name = """
██████╗░░█████╗░███████╗████████╗██████╗░██╗░░░██╗░░░░░░████████╗███████╗░██████╗████████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗░██╔╝░░░░░░╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝██║░░██║█████╗░░░░░██║░░░██████╔╝░╚████╔╝░█████╗░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
██╔═══╝░██║░░██║██╔══╝░░░░░██║░░░██╔══██╗░░╚██╔╝░░╚════╝░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
██║░░░░░╚█████╔╝███████╗░░░██║░░░██║░░██║░░░██║░░░░░░░░░░░░██║░░░███████╗██████╔╝░░░██║░░░
╚═╝░░░░░░╚════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░
"""

console.print(name, style="bold green")

def factorial(n):
    if not n or n is None:
        log("Number is not defined")
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

i = console.input("[bold yellow]Enter number: [/bold yellow]")

console.print(f"\nFactorial number ({i}) : [bold red]{factorial(int(i))}[/bold red]\n", style="bold yellow")
