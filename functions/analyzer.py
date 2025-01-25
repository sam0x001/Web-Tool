from builtwith import builtwith
from colorama import Fore

CYAN = Fore.CYAN
GREEN = Fore.GREEN

def analyze(target):
    info = builtwith(f"http://{target}")
    print(f"{CYAN}\nResults:\n")
    for i in info:
        print(f"{GREEN} {i}",info[i])