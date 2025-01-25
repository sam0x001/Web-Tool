import requests
from colorama import Fore

CYAN = Fore.CYAN
GREEN = Fore.GREEN

def show(target):
    res = requests.head(f"http://{target}")
    headers = res.headers
    print(f"{CYAN}\nResults:\n")
    for i in headers:
        print(f"{GREEN} {i}",headers[i])