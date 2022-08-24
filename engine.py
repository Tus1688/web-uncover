import random
import sys

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from ui import *
from browser import custom_profile

def engine(url, depth, threads, output, user_agent, proxy, cookie):
    try:
        print_info('Url is valid')
        req_headless_browser(url=url, proxy=proxy, depth=int(depth))

    except Exception as e:
        print_error(str(e))
        sys.exit(1)

def req_headless_browser(url, cookie = None, proxy = None, depth:int = 1):
    result = [] # already crawled
    queue = [] # get uri from previously crawled uri and will be used for next request
    trash = [] # out of scope uri
    depth_to_crawl = 3 + depth # depth of crawling
    print_info(f'GET: {url} using headless browser')
    queue.append(url if url.endswith('/') else url + '/')
    comparer = url if url.endswith('/') else url + '/'

    options = Options()
    options.headless = True
    options.profile = custom_profile(proxy)

    driver = webdriver.Firefox(executable_path='geckodriver',options=options)

    # make a recursion to crawl all uri in queue
    while queue:
        url = queue.pop(0)
        # count slash in url if there is # or . in url then - the count of slash by the count of # and .
        count_slash = url.count('/') if '#' not in url else url.count('/') - url.count('#')

        if url.endswith('.md') or url.endswith('.txt'): 
            result.append(url) # add url to result
            continue

        if count_slash == depth_to_crawl:
            # add everything in queue to result
            result.extend(queue)
            break

        print_get_request(url)
        driver.refresh()
        driver.get(url)
        driver.refresh()

        result.append(url) # add url to result
        
        elements = driver.find_elements(By.TAG_NAME, 'a') # get all elemets from current page

        for e in elements:
            temp = e.get_attribute('href') # get href attribute from element
            if (temp is not None): 
                if 'redirect?to=' in temp: # if url is redirect, get redirect url
                    temp = temp.split('redirect?to=')[1]

                if (temp[0:len(comparer)] == comparer): # in scope base url
                    if (temp not in result and temp not in queue):
                        queue.append(temp)
                        print_result_inscope(temp)
                else: # out of scope 
                    if temp not in result and temp not in queue:
                        if temp not in trash: # prevent double print
                            trash.append(temp)
                            print_result_outscope(temp)

    driver.quit()
    print_info('Done\n')

    for i in result:
        print_result_inscope(i)
    print('\n')
    for i in trash:
        print_result_outscope(i)



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
