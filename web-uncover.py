import argparse
import sys
import ipaddress
from ui import bgcolors
from ui import print_banner
from engine import engine


def menu():
    print_banner()
    ap = argparse.ArgumentParser("python3 web-uncover.py")
    ap.add_argument("-u", "--url", required=True, help="url to enumerate")
    ap.add_argument("-d", "--depth", help="depth to enumerate", default=1)
    ap.add_argument("-t", "--threads", help="threads to use", default=10)
    ap.add_argument("-o", "--output", help="output file")

    args = vars(ap.parse_args())

    if not args["url"].startswith("http") and not args["url"].startswith("localhost"):
        print(bgcolors.FAIL + "Invalid url, use http://" + bgcolors.ENDC)
        sys.exit(1)
    else:
        print(bgcolors.OKGREEN + "URL: " + bgcolors.ENDC + bgcolors.OKBLUE + args["url"] + bgcolors.ENDC)
        print(bgcolors.OKGREEN + "Depth: " + bgcolors.ENDC + bgcolors.OKBLUE + str(args["depth"]) + bgcolors.ENDC)
        print(bgcolors.OKGREEN + "Threads: " + bgcolors.ENDC + bgcolors.OKBLUE + str(args["threads"]) + bgcolors.ENDC)
    
    return args

def main():
    args = menu()
    engine(args["url"], args["depth"], args["threads"], args["output"])

if __name__ == "__main__":
    main()
    sys.exit(0)