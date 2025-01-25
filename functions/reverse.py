import socket
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE

def lookup(ip):
    try:
        lookup = socket.gethostbyaddr(ip)
        print(f"{RED} [ ** ]{WHITE} {str(lookup)}")
    except:
        print(f"{RED} [ ! ] {ip} | Not Resolved")