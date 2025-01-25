import socket
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE

def whois(target):
        domain = target.replace("http://", "")
        domain = target.replace("https://", "")
        domain = target.replace("www.", "")
        if domain[-3:] == "org" or domain[-3:] == "com" or domain [-3:] == "net":
            srv = "whois.internic.net"
        else:
            srv = "whois.iana.org"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect((srv, 43))
            s.send((target+"\r\n").encode())
            rs = s.recv(10000).decode()
            print(rs)
        except:
            print(f"{RED} [ ! ] Connection Error")