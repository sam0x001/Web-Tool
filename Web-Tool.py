# Coded with <3 by Sam

import os

try:
    import requests, colorama, socket, builtwith, pythonping, dns
except:
    os.system("pip3 install -r requirements.txt")
    
import sys, os, time, dns, dns.resolver
from sys import platform
from colorama import Fore
from builtwith import builtwith

from functions import ping, whois, admin, ip, reverse, analyzer, ipinfo, subfind, port, headers, ddns
from functions.ip import lookup, lookup_list

RED = Fore.RED
LIGHTRED = Fore.LIGHTRED_EX
GREEN = Fore.GREEN
CYAN = Fore.CYAN
LIGHTGREEN = Fore.LIGHTGREEN_EX
WHITE = Fore.WHITE
RESET = Fore.RESET

def clear():
    os.system('cls') if platform == 'win32' else os.system('clear')

clear()


def main():
    
    clear()
    BANNER = f""" {CYAN}
     _       ____________     __________  ____  __
    | |     / / ____/ __ )   /_  __/ __ \\/ __ \\/ /
    | | /| / / __/ / __  |    / / / / / / / / / /
    | |/ |/ / /___/ /_/ /    / / / /_/ / /_/ / /___
    |__/|__/_____/_____/    /_/  \\____/\\____/_____/
    {LIGHTRED}
                  < .:: WEB-TOOL by Sam ::. >
    < .:: Github & Instagram: sam0x001 | X: Sam00x01 ::. >

    {LIGHTGREEN}
            [ 1 ]   -  Ping Tool
            [ 2 ]   -  Server whois
            [ 3 ]   -  Admin page finder
            [ 4 ]   -  IP lookup
            [ 5 ]   -  Reverse IP lookup
            [ 6 ]   -  Website analyzer
            [ 7 ]   -  IP information
            [ 8 ]   -  Subdomain finder
            [ 9 ]   -  Port scanner
            [ 10 ]  -  Show HTTP headers
            [ 11 ]  -  DNS Resolver
            
            [ 99 ] EXIT

    """
    print(BANNER)

    choose = input(f"{WHITE} WEB-TOOL:~# ")


    ## Ping tool
    if choose == '1':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        ping.ping(target)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Server Whois
    elif choose == '2':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ").lower()
        whois.whois(target)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Admin page finder
    elif choose == '3':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        admin.find(target)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## IP lookup
    elif choose == '4':
        clear()
        
        print("""
            Choose mode:
            1- Single IP lookup
            2- Multi IP lookup
            """)
        
        mode = input(f"{RED} [ + ]{WHITE} Enter your mode:: ")
        
        if mode == '1':
            target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
            lookup(target)
        
        if mode == '2':
            domain_list = input(f"{RED} [ + ]{WHITE} Enter your domain list:: ")   
            lookup_list(domain_list)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Reverse IP lookup
    elif choose == '5':
        clear()
        
        ip = input(f"{RED} [ + ]{WHITE} Enter your Target IP:: ")
        reverse.lookup(ip)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Website technology analyzer
    elif choose == '6':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        analyzer.analyze(target)

        input(f"{CYAN} \n +---END---+")
        main()

    ## IP information
    elif choose == '7':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target IP:: ")
        ipinfo.info(target)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Subdomain finder
    elif choose == '8':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        subfind.find(target)
        
        input(f"{CYAN} \n +---END---+")
        main()

    ## Port scanner
    elif choose == '9':
        clear()

        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        start = int(input(f"{RED} [ + ]{WHITE} Enter start port:: "))
        end = int(input(f"{RED} [ + ]{WHITE} Enter end port:: "))
        print()

        port.scan(target, start, end)
    
        input(f"{CYAN} \n +---END---+")
        main()

    ## Show HTTP headers
    elif choose == '10':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        headers.show(target)
        
        input(f"{CYAN} \n +---END---+")
        main()
    
    ## DNS Resolver
    elif choose == '11':
        clear()
        
        target = input(f"{RED} [ + ]{WHITE} Enter your Target:: ")
        
        if target == '' or ' ' in target:
            print(f"{RED} [ ! ] Target Field can't be empty")
            time.sleep(1)
            main()
        
        NS = input(f"{RED} [ + ]{WHITE} Enter your DNS Address(default is 8.8.8.8):: ")
        
        if NS == '' or ' ' in NS:
            NS = "8.8.8.8"
        
        print(f"""{WHITE}
        Choose a record:
              1- A             6- CNAME        11- NS
              2- AAAA          7- DNAME        12- TXT
              3- AFSDB         8- DNSKEY
              4- CAA           9- IPSECKEY
              5- CERT          10- MX
              """)
        record = input(f"{RED} [ + ]{WHITE} Enter Record type:: ")
        
        if record == '1':
            record = "A"
        elif record == '2':
            record = "AAAA"
        elif record == '3':
            record = "AFSDB"
        elif record == '4':
            record = "CAA"
        elif record == '5':
            record = "CERT"
        elif record == '6':
            record = "CNAME"
        elif record == '7':
            record = "DNAME"
        elif record == '8':
            record = "DNSKEY"
        elif record == '9':
            record = "IPSECKEY"
        elif record == '10':
            record = "MX"
        elif record == '11':
            record = "NS"
        elif record == '12':
            record = "TXT"
        else:
            print(f"{RED} [ ! ] Record type is not valid")
            time.sleep(1)
            main()
        
        ddns.resolve(target, record, NS)

        input(f"{CYAN} \n +---END---+")
        main()
    
    elif choose == '99':
        print(RESET)
        clear()
        exit()

    else:
        clear()
        print(f" {RED}[ ! ] Please choose a valid option")
        time.sleep(1)
        main()

main()