import requests
import re
def get_page(url):
    proxies = {
        "http":"http://114.225.170.90:53128",
        "https":"https//114.225.170.90:53128",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        return req.text
    else:
        return None
def main():
    url = 'http://maoyan.com/board/4'
    url = "http://www.xicidaili.com/nn"
    html = get_page(url)
    #print(html)
    pattern = '<a href="/films.*?title="(.*?)".*?">(.*?)</a>.*?">(.*?)</p>.*?">(.*?)</p>.*?integer.*?>(.*?)</i>.*?'

    pattern = '(?=(\\b|\D))(((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))(?=(\\b|\D))'
    r = re.search(pattern, html, re.S)
    print(r)
    r = re.findall(pattern, html, re.S)
    for l in r:
        print(l)

main()

