import requests
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE
GREEN = Fore.GREEN

def find(target):
    try:
        get_file = input(f"{RED} [ + ]{WHITE} Enter your Subdomain file(press enter to use default):: ")
        file = open(get_file)
    except:
        file = open("files/subdomain.txt")
        
    content = file.read()
    subs = content.splitlines()
    for subdomain in subs:
        url = f"http://{subdomain}.{target}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        except KeyboardInterrupt:
            print(f"{RED} [ ! ] Process Interrupted")
        else:
            print(f"{GREEN} [ DISCOVERED ] {url}")