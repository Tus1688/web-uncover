import random
import sys

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ui import print_error, print_info

initial_cookie = [{}] # cookie from first request / provided by user

def engine(url, depth, threads, output, user_agent, proxy, cookie):
    try:
        r = requests.get(url)
        print_info('Url is valid')
        req_headless_browser(url)
    except Exception as e:
        print_error(str(e))
        sys.exit(1)

def req_headless_browser(url, cookie = None):
    print_info(f'Requesting {url} using headless browser')
    options = Options()
    options.headless = True

    options.add_argument('--disable-cache')
    options.add_argument('--disable-telemetry')
    # options resist fingerprinting
    options.add_argument('--lang=en-US')
    options.add_argument('--disable-client-side-phishing-detection')

    driver = webdriver.Firefox(executable_path='geckodriver',options=options)
    driver.delete_all_cookies()

    # use custom user agent from getUserAgent()
    driver.execute_script("window.navigator.userAgent = '{}'".format(getUserAgent(True)))

    # prevent browser to be fingerprinted
    driver.execute_script("window.navigator.webdriver = false")
    driver.execute_script("window.navigator.languages = ['en-US', 'en']")
    driver.execute_script("window.navigator.platform = '{}'".format(random.choice(['MacIntel', 'Win32', 'Linux x86_64'])))
    driver.execute_script("window.navigator.product = '{}'".format(random.choice(['Gecko', 'Gecko/20100101 Firefox/{}'.format(random.randint(1, 60))])))
    driver.execute_script("window.navigator.productSub = '{}'".format(random.choice(['20030107', '20100101', '20100101', '20100101'])))
    driver.execute_script("window.navigator.vendor = '{}'".format(random.choice(['Mozilla', 'Mozilla/5.0'])))
    driver.execute_script("window.navigator.vendorSub = '{}'".format(random.choice(['20100101', '20100101', '20100101', '20100101'])))
    driver.execute_script("window.navigator.buildID = '{}'".format(random.choice(['20100101', '20100101', '20100101', '20100101'])))

    driver.get(url)

    html_result = driver.page_source
    #print(html_result)
    initial_cookie = driver.get_cookies()

    driver.close()
    # print request and response

    for cookie in initial_cookie:
        print(cookie)

def req_python_request(url, cookie):
    print_info(f'Requesting {url} using python requests')
    headers = {
        'User-Agent': getUserAgent(True),
        'Cookie': cookie
    }
    r = requests.get(url, headers=headers)
    print(r.text)

def getUserAgent(value:bool = False) -> str:
    if value:
        # user agent from user-agents.txt file and ignore line starting with #
        with open('user-agents.txt', 'r') as f:
            user_agents = [line.strip() for line in f if not line.startswith('#')]
            return random.choice(user_agents)
    else:
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
