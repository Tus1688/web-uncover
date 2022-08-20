import random
import sys

import requests

from ui import print_error, print_info

cookie = "" # cookie from first request / provided by user

def engine(url, depth, threads, output, user_agent, proxy, cookie):
    print("\nfrom engine.py \n")
    print(url, depth, threads, output, user_agent)
    print(getUserAgent(False))
    
    try:
        r = requests.get(url)
        print_info('Url is valid')
        curl(url)
    except Exception as e:
        print_error(str(e))
        sys.exit(1)

def curl(url):
    # make request with custom user agent
    headers = getUserAgent()
    r = requests.get(url, headers=headers)
    # make another request with r cookies
    r2 = requests.get(url, headers=headers, cookies=r.cookies)

def getUserAgent(value:bool = False) -> str:
    if value:
        # user agent from user-agents.txt file and ignore line starting with #
        with open('user-agents.txt', 'r') as f:
            user_agents = [line.strip() for line in f if not line.startswith('#')]
            return random.choice(user_agents)
    else:
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
