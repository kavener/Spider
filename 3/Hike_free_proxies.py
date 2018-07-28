import requests
import re
def ip_test():
            proxies = ip_draw()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
            }
            for proxy in proxies:
                try:
                    r = requests.get('https://www.baidu.com', headers=headers, proxies=proxy,timeout = 2)
                    print(r.status_code)
                    if r.status_code == 200:
                        with open("useful_ip.text", 'a') as f:
                            f.writelines(proxy['http'])
                except:

                    print("IP有问题？？？")
def ip_draw():
    proxies = []
    with open('free_proxies.txt', 'r') as f:
        for line in f.readlines():
            try:
                result = re.match('(^\d.*?)\n',line)
                # print(result.group(1))
                proxy = {
                    "http": "http://" + str(result.group(1)),
                    "https": "https://" + str(result.group(1)),
                }
            except:
                continue


            proxies.append(proxy)
        return proxies
ip_test()