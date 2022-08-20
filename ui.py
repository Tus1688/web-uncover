class bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    print(bgcolors.HEADER + """
============================================
*       enumerate faster == profits        *
*  https://github.com/Tus1688/web-uncover  *
============================================
    """ + bgcolors.ENDC)

def print_info(info):
    print(bgcolors.OKGREEN + "[*] INFO: " + bgcolors.ENDC + info)

def print_error(error):
    print(bgcolors.FAIL + "[-] Error: " + bgcolors.ENDC + error)