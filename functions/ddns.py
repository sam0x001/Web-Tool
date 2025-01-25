import dns, dns.resolver
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE


def resolve(target, record, NS):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [NS]
        
    print()
        
    try:

        result = resolver.resolve(target, record)
        for rdata in result:
            print(f"{RED} [ + ]{WHITE} {record}\t|\t{rdata}")

    except dns.resolver.NXDOMAIN:
        print(f"{RED} [ ! ] {record}\t|\tNOT EXIST")

    except dns.resolver.NoAnswer:
        print(f"{RED} [ ! ] {record}\t|\tNO ANSWER")

    except dns.resolver.NoNameservers:
        print(f"{RED} [ ! ] {record}\t|\tNO NAMESERVERS")

    except dns.exception.Timeout:
        print(f"{RED} [ ! ] {record}\t|\tTIMEOUT")

    except dns.resolver.NoRootSOA:
        print(f"{RED} [ ! ] {record}\t|\tNO ROOT SOA")