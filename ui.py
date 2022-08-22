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
                             __                                                                                   
                        /  |                                                                                  
 __   __   __   ______  $$ |____         __    __  _______    _______   ______   __     __  ______    ______  
/  | /  | /  | /      \ $$      \       /  |  /  |/       \  /       | /      \ /  \   /  |/      \  /      \ 
$$ | $$ | $$ |/$$$$$$  |$$$$$$$  |      $$ |  $$ |$$$$$$$  |/$$$$$$$/ /$$$$$$  |$$  \ /$$//$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$    $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ | $$  /$$/ $$    $$ |$$ |  $$/ 
$$ \_$$ \_$$ |$$$$$$$$/ $$ |__$$ |      $$ \__$$ |$$ |  $$ |$$ \_____ $$ \__$$ |  $$ $$/  $$$$$$$$/ $$ |      
$$   $$   $$/ $$       |$$    $$/       $$    $$/ $$ |  $$ |$$       |$$    $$/    $$$/   $$       |$$ |      
 $$$$$/$$$$/   $$$$$$$/ $$$$$$$/         $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$/      $/     $$$$$$$/ $$/       
                                                                                                              
    """ + bgcolors.ENDC)

def print_info(info):
    print(bgcolors.OKGREEN + "[*] INFO: " + bgcolors.ENDC + info)

def print_error(error):
    print(bgcolors.FAIL + "[-] Error: " + bgcolors.ENDC + error)

def print_result_inscope(value):
    print("["+ bgcolors.OKGREEN + "*" + bgcolors.ENDC + "] IN SCOPE: " + value)

def print_result_outscope(value):
    print("["+ bgcolors.FAIL + "-" + bgcolors.ENDC + "] OUT OF SCOPE: " + value)

def print_get_request(url):
    print(bgcolors.HEADER + "[*] GET: " + bgcolors.ENDC + url)