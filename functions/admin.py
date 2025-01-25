import requests
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE
GREEN = Fore.GREEN

def find(target):
    
    try:
            
        try:
            get_file = input(f"{RED} [ + ]{WHITE} Import your URL file (press enter to use default):: ")
            urlfile = open(get_file)
        except:
            urlfile = open("files/login.txt")
            
        status = input(f"{RED} [ + ]{WHITE} Skip other status codes except 200?[Y/n]: ")
            
        if not target.startswith("http://") or not target.startswith("https://"):
            target  = "http://" + target
        
        print("\n")
        
        for url in urlfile:
            url = url.strip("\n")
            full_address = target + "/" + url
            response = requests.get(full_address)
                
            if status.lower() == 'n' or status.lower() == 'no':
                if response.status_code == 200:
                    print(f"{GREEN} [ 200 ] {full_address}")
                else:
                    print(f"{WHITE} [ {response.status_code} ] {full_address}")

            elif status.lower() == 'y' or status.lower() == 'yes' or status == '':
                if response.status_code == 200:
                    print(f"{GREEN} [ 200 ] {full_address}")
                else:
                    pass
                
            else:
                print(f"{RED} [ ! ] Invaild answer")
                time.sleep(1)
                
    except requests.ConnectionError:
        print(f"{RED} [ ! ] Please check your Internet connection or Domain")
    except KeyboardInterrupt:
        print(f"{RED} [ ! ] Process Interrupted")