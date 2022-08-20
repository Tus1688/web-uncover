import argparse
import sys

from engine import engine
from ui import bgcolors, print_banner


def menu():
    print_banner()
    ap = argparse.ArgumentParser("python3 web-uncover.py")
    ap.add_argument("-u", "--url", required=True, help="url to enumerate")
    ap.add_argument("-d", "--depth", help="depth to enumerate", default=1)
    ap.add_argument("-t", "--threads", help="threads to use", default=10)
    ap.add_argument("-o", "--output", help="output file")
    ap.add_argument("-ua", "--user-agent", help="user agent to use")
    ap.add_argument("-p", "--proxy", help="proxy to use")
    ap.add_argument("-c", "--cookie", help="cookie to use")

    args = vars(ap.parse_args())

    if not args["url"].startswith("http") and not args["url"].startswith("localhost"):
        print(bgcolors.FAIL + "Invalid url, use http://" + bgcolors.ENDC)
        sys.exit(1)
    else:
        print(bgcolors.OKGREEN + "[*] URL: " + bgcolors.ENDC + bgcolors.OKBLUE + args["url"] + bgcolors.ENDC)
        print(bgcolors.OKGREEN + "[*] Depth: " + bgcolors.ENDC + bgcolors.OKBLUE + str(args["depth"]) + bgcolors.ENDC)
        print(bgcolors.OKGREEN + "[*] Threads: " + bgcolors.ENDC + bgcolors.OKBLUE + str(args["threads"]) + bgcolors.ENDC)
        if args["proxy"]:
            print(bgcolors.OKGREEN + "[*] Proxy: " + bgcolors.ENDC + bgcolors.OKBLUE + args["proxy"] + bgcolors.ENDC)
        if args["user_agent"] is None:
            print(bgcolors.OKGREEN + "[*] User Agent: " + bgcolors.ENDC + bgcolors.OKBLUE + "Default" + bgcolors.ENDC)
        if args["cookie"] is None:
            print(bgcolors.OKGREEN + "[*] Cookie: " + bgcolors.ENDC + bgcolors.OKBLUE + "Not provided" + bgcolors.ENDC)
    
    return args

def main():
    args = menu()
    engine(url=args["url"],depth=args["depth"],threads=args["threads"],
        output=args["output"],user_agent=args["user_agent"],proxy=args["proxy"],cookie=args["cookie"])

if __name__ == "__main__":
    main()
    sys.exit(0)
