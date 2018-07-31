import requests
import re
url = 'http://wenshu.court.gov.cn/List/ListContent'

Request_headers = '''
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7
Connection: keep-alive
Content-Length: 240
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _gscu_2116842793=32182710w1ghhu79; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1532182710,1532672323,1533042266; _gscbrs_2116842793=1; vjkl5=c5be62ee09bffd7f04f01a618dbba5d058545893; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1533049048; _gscs_2116842793=t33049048d6z6bs19|pv:1
Host: wenshu.court.gov.cn
Origin: http://wenshu.court.gov.cn
Referer: http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
form_data = '''
Param: 案件类型:民事案件
Index: 9
Page: 5
Order: 法院层级
Direction: asc
vl5x: 69b68b41342d7b787b7a10d0
number: VHQ8GYC7
guid: 532a43e7-2bc3-0233df72-cb963bb3dcb1
'''

def request_format(Request_headers):
    headers={}
    pattern = re.compile('\\n(.*?): (.*?)\\n', re.S)
    times = Request_headers.count('\n') - 2
    while times >= 0:
        result = re.search(pattern, Request_headers)
        Request_headers = Request_headers[Request_headers.index('\n')+2:]
        headers[result.group(1)]=result.group(2)
        times = times - 1
    return headers
headers = request_format(Request_headers)
data = request_format(form_data)
print(headers)
print(data)
response = requests.get(url=url, headers=headers, params=data)
print(response.status_code)


