import requests
from colorama import Style, Fore

welcomeMsg = '''
  ___   ____            ___            __         
 |_ _| |  _ \          |_ _|  _ __    / _|   ___  
  | |  | |_) |  _____   | |  | '_ \  | |_   / _ \ 
  | |  |  __/  |_____|  | |  | | | | |  _| | (_) |
 |___| |_|             |___| |_| |_| |_|    \___/ 
 Gather info about ip addresses.                                                 
'''

print(f'{Fore.BLUE}{welcomeMsg}{Style.RESET_ALL}')


def start():
    ip_address = input("Input an ip address: ")

    response = requests.get(f"http://ip-api.com/json/{ip_address}").json()

    if response['status'] == "success":
        pass
    else:
        print(f'{Fore.RED}Invalid ip address...{Style.RESET_ALL}')
        quit(1)

    print(f'{Fore.BLUE}Country: {Fore.GREEN}{response["country"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Region: {Fore.GREEN}{response["regionName"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}City: {Fore.GREEN}{response["city"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Zip code: {Fore.GREEN}{response["zip"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Latitude: {Fore.GREEN}{response["lat"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Longitude: {Fore.GREEN}{response["lon"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Timezone: {Fore.GREEN}{response["timezone"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}ISP: {Fore.GREEN}{response["isp"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}ORG: {Fore.GREEN}{response["org"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}AS: {Fore.GREEN}{response["as"]}{Style.RESET_ALL}')
    print(f'{Fore.BLUE}Query: {Fore.GREEN}{response["query"]}{Style.RESET_ALL}')


while True:
    start()
