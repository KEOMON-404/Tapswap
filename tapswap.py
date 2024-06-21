# DECODE BY:- JOKER > @EZ_X4 # COPYRIGHT:- @JOKERTOOLZZ

import os
import requests
from colorama import Fore  
from urllib.parse import urlparse, parse_qs
from time import sleep 
os.system("clear")
print(Fore.RED +"""

┏━━━┓╋╋╋╋╋╋╋╋╋┏━━━━┓
┃┏━┓┃╋╋╋╋╋╋╋╋╋┃┏┓┏┓┃
┃┗━━┳┓┏┓┏┳━━┳━┻┫┃┃┣┻━┳━━┓
┗━━┓┃┗┛┗┛┃┏┓┃┏┓┃┃┃┃┏┓┃┏┓┃
┃┗━┛┣┓┏┓┏┫┏┓┃┗┛┃┃┃┃┏┓┃┗┛┃
┗━━━┛┗┛┗┛┗┛┗┫┏━┛┗┛┗┛┗┫┏━┛
╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋┗┛╋╋╋╋╋╋╋┗┛
Dec By JOKER > @EZ_X4""")
url = input(f"{Fore.GREEN}welcome to swap tap auto miner\n\n{Fore.BLUE}please paste your link here : ")
def MINE(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.fragment)
    tgWebAppData = query_params.get('tgWebAppData', [None])[0]
    url = 'https://api.tapswap.ai/api/account/login'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://app.tapswap.ai',
        'Pragma': 'no-cache',
        'Referer': 'https://app.tapswap.ai/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-app': 'tapswap_server',
        'x-cv': '1',
    }
    
    
    data = {
        'init_data':tgWebAppData, 
        'referrer': ''
    }
    
    response = requests.post(url, headers=headers, json=data)
    infot = response.json()
    token = infot['access_token']
    player = infot['player']
    energy = player['energy']
    url = 'https://api.tapswap.ai/api/player/submit_taps'
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Authorization': f'Bearer {token}',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Id': '2069730816',
    'Content-Type': 'application/json',
    'Origin': 'https://app.tapswap.club',
    'Pragma': 'no-cache',
    'Referer': 'https://app.tapswap.club/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-app': 'tapswap_server',
    'x-cv': '1',
    }

    data = {"taps":5000,"time":171519077742}
    
    response = requests.post(url, headers=headers, json=data)
    player = response.json()
    print(player)
    print(Fore.CYAN +f" taps : {energy}   " , end="")
    
total = 0   
while True : 
    try:
        MINE(url)
        total= total + 1
        print("thread : " ,total)
        sleep(0)
    except KeyboardInterrupt :
        print(Fore.CYAN +"Thanks for using check our channel for more miner tools t.me/swaptapnews")
        break
    except:
        print(Fore.RED + f"Something went wrong try again; if it continues report at {Fore.BLUE} t.me/swaptapnews")
        break
    
        

