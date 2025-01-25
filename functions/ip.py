import socket, time
from colorama import Fore

RED = Fore.RED
GREEN = Fore.LIGHTGREEN_EX
WHITE = Fore.WHITE

def lookup(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{RED} [ ** ]{GREEN} Hostname: {target} | IP: {ip}")
    except:
        print(f"{RED} [ ! ] Please check your Internet Connection or Domain")

def lookup_list(domain_list):
    print("\n")
    try:
        try:
            file = open(domain_list)
        except:
            print(f"{RED} [ ! ] File does not exist")
            time.sleep(1)
            
        with open(domain_list, 'r') as file:
            domains = file.readlines()
        
        domains = [x.strip() for x in domains]
    
        for domain in domains:
            try:
                domain_ip = socket.gethostbyname(domain)
                print(f"{RED} [ ** ]{GREEN} {domain}\t|\t{domain_ip}")
            except socket.gaierror:
                print(f"{RED} [ ** ] {domain}\t|\tNot resolved")
    
    except KeyboardInterrupt:
        print(f"\n{RED} [ ! ] Process Interrupted")