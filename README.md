# web-uncover
web-uncover is a web enumeration tool that automates the process of detecting subdirectory by parsing href in html

usage: 
```
python3 web-uncover.py -u [URL] -d [DEPTH OF CRAWL] -p [PROXY] 
```

example:
```
$ python3 web-uncover.py -u https://juice-shop.herokuapp.com -d 1

                             __
                        /  |
 __   __   __   ______  $$ |____         __    __  _______    _______   ______   __     __  ______    ______
/  | /  | /  | /      \ $$      \       /  |  /  |/       \  /       | /      \ /  \   /  |/      \  /      \
$$ | $$ | $$ |/$$$$$$  |$$$$$$$  |      $$ |  $$ |$$$$$$$  |/$$$$$$$/ /$$$$$$  |$$  \ /$$//$$$$$$  |/$$$$$$  |
$$ | $$ | $$ |$$    $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ | $$  /$$/ $$    $$ |$$ |  $$/
$$ \_$$ \_$$ |$$$$$$$$/ $$ |__$$ |      $$ \__$$ |$$ |  $$ |$$ \_____ $$ \__$$ |  $$ $$/  $$$$$$$$/ $$ |
$$   $$   $$/ $$       |$$    $$/       $$    $$/ $$ |  $$ |$$       |$$    $$/    $$$/   $$       |$$ |
 $$$$$/$$$$/   $$$$$$$/ $$$$$$$/         $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$/      $/     $$$$$$$/ $$/


[*] URL: https://juice-shop.herokuapp.com
[*] Depth: 1
[*] Threads: 1
[*] User Agent: Default
[*] Cookie: Not provided
[*] INFO: Url is valid
Do you want to use headless browser? (y/n) y
[*] INFO: GET: https://juice-shop.herokuapp.com using headless browser
[*] GET: https://juice-shop.herokuapp.com/
[-] OUT OF SCOPE: https://www.youtube.com/watch?v=9PnbKL3wuH4
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/login
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/contact
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/about
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/photo-wall
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/score-board
[-] OUT OF SCOPE: https://github.com/bkimminich/juice-shop
[-] OUT OF SCOPE: https://owasp.org/
[-] OUT OF SCOPE: https://owasp-juice.shop/
[*] GET: https://juice-shop.herokuapp.com/#/login
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/forgot-password
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/register
[*] GET: https://juice-shop.herokuapp.com/#/contact
[*] GET: https://juice-shop.herokuapp.com/#/about
[*] IN SCOPE: https://juice-shop.herokuapp.com/ftp/legal.md
[*] IN SCOPE: https://juice-shop.herokuapp.com/#!
[-] OUT OF SCOPE: https://twitter.com/owasp_juiceshop
[-] OUT OF SCOPE: https://www.facebook.com/owasp.juiceshop
[-] OUT OF SCOPE: https://owasp.org/slack/invite
[-] OUT OF SCOPE: https://www.reddit.com/r/owasp_juiceshop
[-] OUT OF SCOPE: https://github.com/OWASP/owasp-swag/tree/master/projects/juice-shop
[*] GET: https://juice-shop.herokuapp.com/#/photo-wall
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=%F0%9F%98%BC%20#zatschi%20#whoneedsfourlegs%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=Magn(et)ificent!%20(%C2%A9%20bkimminich)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=My%20rare%20collectors%20item!%20[%CC%B2%CC%85$%CC%B2%CC%85(%CC%B2%CC%85%20%CD%A1%C2%B0%20%CD%9C%CA%96%20%CD%A1%C2%B0%CC%B2%CC%85)%CC%B2%CC%85$%CC%B2%CC%85]%20(%C2%A9%20bkimminich)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=I%20love%20going%20hiking%20here...%20(%C2%A9%20j0hNny)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=My%20old%20workplace...%20(%C2%A9%20E=ma%C2%B2)%20@owasp_juiceshop&hashtags=appsec
[*] GET: https://juice-shop.herokuapp.com/#/score-board
[-] OUT OF SCOPE: http://gitter.im/bkimminich/juice-shop
[-] OUT OF SCOPE: https://github.com/bkimminich/juice-shop/issues
[*] GET: https://juice-shop.herokuapp.com/#/forgot-password
[*] GET: https://juice-shop.herokuapp.com/#/register
[*] GET: https://juice-shop.herokuapp.com/#!
[*] INFO: Done

[*] IN SCOPE: https://juice-shop.herokuapp.com/
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/login
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/contact
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/about
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/photo-wall
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/score-board
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/forgot-password
[*] IN SCOPE: https://juice-shop.herokuapp.com/#/register
[*] IN SCOPE: https://juice-shop.herokuapp.com/ftp/legal.md
[*] IN SCOPE: https://juice-shop.herokuapp.com/#!


[-] OUT OF SCOPE: https://www.youtube.com/watch?v=9PnbKL3wuH4
[-] OUT OF SCOPE: https://github.com/bkimminich/juice-shop
[-] OUT OF SCOPE: https://owasp.org/
[-] OUT OF SCOPE: https://owasp-juice.shop/
[-] OUT OF SCOPE: https://twitter.com/owasp_juiceshop
[-] OUT OF SCOPE: https://www.facebook.com/owasp.juiceshop
[-] OUT OF SCOPE: https://owasp.org/slack/invite
[-] OUT OF SCOPE: https://www.reddit.com/r/owasp_juiceshop
[-] OUT OF SCOPE: https://github.com/OWASP/owasp-swag/tree/master/projects/juice-shop
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=%F0%9F%98%BC%20#zatschi%20#whoneedsfourlegs%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=Magn(et)ificent!%20(%C2%A9%20bkimminich)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=My%20rare%20collectors%20item!%20[%CC%B2%CC%85$%CC%B2%CC%85(%CC%B2%CC%85%20%CD%A1%C2%B0%20%CD%9C%CA%96%20%CD%A1%C2%B0%CC%B2%CC%85)%CC%B2%CC%85$%CC%B2%CC%85]%20(%C2%A9%20bkimminich)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=I%20love%20going%20hiking%20here...%20(%C2%A9%20j0hNny)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: https://twitter.com/intent/tweet?text=My%20old%20workplace...%20(%C2%A9%20E=ma%C2%B2)%20@owasp_juiceshop&hashtags=appsec
[-] OUT OF SCOPE: http://gitter.im/bkimminich/juice-shop
[-] OUT OF SCOPE: https://github.com/bkimminich/juice-shop/issues
```

# Disclaimer 
Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user’s responsibility to obey all applicable local, state and federal laws. We assume no liability and are not responsible for any misuse or damage caused by this tool.
