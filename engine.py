import random
import sys

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from ui import print_error, print_info, print_result_incope, print_result_outscope
from browser import custom_profile

initial_cookie = [{}] # cookie from first request / provided by user
# inscope uri 
final_uri = [] # already crawled
queue = [] # get uri from previously crawled uri and will be used for next request


def engine(url, depth, threads, output, user_agent, proxy, cookie):
    try:
        print_info('Url is valid')
        req_headless_browser(url=url)

    except Exception as e:
        print_error(str(e))
        sys.exit(1)

def req_headless_browser(url, cookie = None, proxy = None):
    print_info(f'GET: {url} using headless browser')

    options = Options()
    options.headless = True
    options.profile = custom_profile(proxy)

    driver = webdriver.Firefox(executable_path='geckodriver',options=options)
    driver.get(url)

    final_uri.append(url)

    elements = driver.find_elements(by=By.TAG_NAME, value="*")
    for e in elements:
        temp = e.get_attribute('href')
        url_length = len(url)
        if (temp is not None):
            if 'redirect?to=' in temp:
                temp = temp.split('redirect?to=')[1]

            if (temp[0:url_length] == url):
                if temp not in final_uri:
                    queue.append(temp)
                    print_result_incope(temp)
            else:
                print_result_outscope(temp)


    initial_cookie = driver.get_cookies()
    driver.quit()


def req_python_request(url, cookie= None, proxy = None):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': getUserAgent(True)
        }
    destruct_proxy = {'http': f'http://{proxy}', 'https': f'https://{proxy}'} if proxy else {}

    r = requests.get(url=url, headers=headers, proxies=destruct_proxy,verify=False)
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
