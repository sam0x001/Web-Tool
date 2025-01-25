import requests

def info(target):
    url = f"https://ipinfo.io/{target}/json"
    get = requests.get(url)
    text = get.text
    print("\n" + text)