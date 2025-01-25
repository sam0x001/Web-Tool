import pythonping
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE

def ping(target):
        number = int(input(f"{RED} [ + ]{WHITE} Enter number of packets:: "))
        size = int(input(f"{RED} [ + ]{WHITE} Enter the size of packets:: "))
        ping = pythonping.ping(target, verbose=True, count=number, size=size)