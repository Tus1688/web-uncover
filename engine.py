import random
import sys

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from urllib3.exceptions import InsecureRequestWarning

from browser import custom_profile
from ui import *

# surpress ssl warning for urlib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def engine(url, depth, threads, output, user_agent, proxy, cookie):
    try:
        print_info('Url is valid')
        inp = input('Do you want to use headless browser? (y/n) ')
        if inp == 'y':
            req_headless_browser(url=url,proxy=proxy, depth=int(depth))
        else:
            req_python_request(url=url, proxy=proxy, depth=int(depth))
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
        count_slash = (url.count('/') 
            if '#/' not in url  and './' not in url and '!/' not in url
            else url.count('/') - url.count('#/') - url.count('./') - url.count('!/'))

        if url.endswith('.md') or url.endswith('.txt'): 
            result.append(url) # add url to result
            continue

        if count_slash == depth_to_crawl:
            # add everything in queue to result
            result.extend(queue)
            break # stop crawling

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



def req_python_request(url, cookie= None, proxy = None, depth:int = 1):
    list_of_accept_header = ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "*/*"]
    result = [] # already crawled
    queue = [] # get uri from previously crawled uri and will be used for next request
    trash = [] # out of scope uri
    depth_to_crawl = 3 + depth # depth of crawling

    print_info(f'GET: {url} using python request')
    queue.append(url if url.endswith('/') else url + '/')
    comparer = url if url.endswith('/') else url + '/'

    def request_local():
        headers = {
            'Accept': list_of_accept_header[random.randint(0, len(list_of_accept_header) - 1)],
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': getUserAgent(True)
            }
        destruct_proxy = {'http': f'http://{proxy}', 'https': f'https://{proxy}'} if proxy else {}

        print_get_request(url)

        r = requests.get(url=url, headers=headers, proxies=destruct_proxy,verify=False)

        result.append(url) # add url to result

        soup = BeautifulSoup(r.text, 'html.parser')
        elements = soup.find_all('a')
        
        for e in elements:
            temp = e.get('href')
            if (temp is not None): 
                if 'redirect?to=' in temp:
                    temp = temp.split('redirect?to=')[1]

                if ("http://" not in temp and "https://" not in temp):
                    temp = comparer + temp

                if (temp[0:len(comparer)] == comparer): # in scope base url
                    if (temp not in result and temp not in queue):
                        queue.append(temp)
                        print_result_inscope(temp)
                else: # out of scope
                    if temp not in result and temp not in queue:
                        if temp not in trash:
                            trash.append(temp)
                            print_result_outscope(temp)

    while queue:
        url = queue.pop(0)
        count_slash = (url.count('/') 
            if '#/' not in url  and './' not in url and '!/' not in url
            else url.count('/') - url.count('#/') - url.count('./') - url.count('!/'))

        if url.endswith('.md') or url.endswith('.txt'): 
            result.append(url) # add url to result
            continue

        if count_slash == depth_to_crawl:
            # add everything in queue to result
            result.extend(queue)
            break # stop crawling
        
        request_local()

    # count result if 1
    if len(result) == 1:
        print_info("It's seems that there is no link in this page, or you can try to use headless browser")
        sys.exit(1)
    print_info('Done\n')

    for i in result:
        print_result_inscope(i)
        if "ajax" in i or "AJAX" in i or "javascript:" in i:
            print_info("AJAX is needed for this link ^^ to get a better result, you can try to combined it using headless browser")
    print('\n')
    for i in trash:
        print_result_outscope(i)
    
    
            
    


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
