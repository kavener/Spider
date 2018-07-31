import requests
import re
url = 'http://wenshu.court.gov.cn/List/ListContent'

Request_headers = '''
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7
Connection: keep-alive
Content-Length: 213
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: _gscu_2116842793=32182710w1ghhu79; _gscbrs_2116842793=1; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1532182710,1532672323,1533042266,1533049479; vjkl5=aa2af9bffdff0b901ea1859f5bde66c280662e55; _gscs_2116842793=t33049048d6z6bs19|pv:6; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1533049529
Host: wenshu.court.gov.cn
Origin: http://wenshu.court.gov.cn
Referer: http://wenshu.court.gov.cn/list/list/?sorttype=1&number=87NDDC77&guid=7fc5fe6d-67db-585b87fa-e8cb13c3817b&conditions=searchWord+%E5%90%88%E5%90%8C+++%E5%85%B3%E9%94%AE%E8%AF%8D:%E5%90%88%E5%90%8C
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
form_data = '''
Param: 关键词:合同
Index: 9
Page: 5
Order: 法院层级
Direction: asc
vl5x: 37bc203a772b49940808dda5
number: 5Q895295
guid: 04768aee-6a5d-d55e776d-9f2159814e0a
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

response = requests.post(url='http://wenshu.court.gov.cn/List/ListContent', headers=headers, data=data)
print(response.text)


