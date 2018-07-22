import requests

with open('free_proxies.txt', 'r') as f:
    for line in f.readlines():
        proxies = {
            "http": "http://" + line,
            "https": "https://" + line,
        }
        r = requests.get('https://www.python.org', proxies=proxies)
