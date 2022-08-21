import random
import sys

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ui import print_error, print_info
from browser import custom_profile

initial_cookie = [{}] # cookie from first request / provided by user

def engine(url, depth, threads, output, user_agent, proxy, cookie):
    try:
        print_info('Url is valid')
        req_headless_browser(url=url, proxy="127.0.0.1:8080")
        #req_python_request(url=url,proxy="https://127.0.0.1:8080")
    except Exception as e:
        print_error(str(e))
        sys.exit(1)

def req_headless_browser(url, cookie = None, proxy = None):
    print_info(f'GET: {url} using headless browser')

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(executable_path='geckodriver',options=options, firefox_profile=custom_profile(proxy, getUserAgent(False)))
    driver.get(url)

    html_result = driver.page_source
    print(html_result)
    initial_cookie = driver.get_cookies()

    driver.quit()

    for cookie in initial_cookie:
        print(cookie)

def req_python_request(url, cookie= None, proxy = None):
    headers = {'Accept': '*/*', 'User-Agent': getUserAgent(True)}
    r = requests.get(url=url, headers=headers, proxies={'http': proxy, 'https': proxy},verify=False)
    # get cookies from response
    initial_cookie = r.cookies.get_dict()
    for cookie in initial_cookie:
        print(cookie)

def getUserAgent(value:bool = False) -> str:
    if value:
        # user agent from user-agents.txt file and ignore line starting with #
        with open('user-agents.txt', 'r') as f:
            user_agents = [line.strip() for line in f if not line.startswith('#')]
            random_user_agent = random.choice(user_agents)
            print_info(f'Using user agent: {random_user_agent}')
            return random_user_agent 
    else:
        print_info('Using user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
