import socket
from colorama import Fore

RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE

def scan(target, start, end):
    try:  

        for port in range(start, end+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
    
            result = s.connect_ex((target,port))

            if result ==0:
                print(f" {RED}[ * ]{GREEN} {target}:{port} {WHITE}/TCP Open")
                s.close()
    
    except KeyboardInterrupt:
        print(f"\n {RED}[ ! ] Process Interrupted")
    
    except socket.gaierror:
        print(f"\n {RED}[ ! ] Hostname Could Not Be Resolved")
    
    except socket.error:
        print(f"\n {RED}[ ! ] Server not responding")
