import requests
import sys
from bs4 import BeautifulSoup
from ui import bgcolors

def engine(url, depth, threads, output):
    print("from engine.py")
    try:
        r = requests.get(url)
    except Exception as e:
        print(bgcolors.FAIL + "Error: " + str(e) + bgcolors.ENDC)
        sys.exit(1)

    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.prettify())