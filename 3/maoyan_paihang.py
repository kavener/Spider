import requests

def get_page(url):
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
    html = get_page(url)
    print(html)
    pattern = '<a href="/films.*?title="(.*?)".*?">(.*?)</a>.*?">(.*?)</p>.*?">(.*?)</p>.*?integer.*?>(.*?)</i>.*?'

main()

