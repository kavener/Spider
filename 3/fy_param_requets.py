import requests
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
data = {
    'Param': '关键词:第三人',
    'Index': '4',
    'Page': '5',
    'Order': '法院层级',
    'Direction': 'asc',
    'vl5x': '22cbc096c900486f74e32da5',
    'number': 'JE8XZVLL',
    'guid': '2b5f0a75-f9ac-ed01677c-8af00d1c3f9b'
}
response = requests.post("http://wenshu.court.gov.cn/List/ListContent", headers=headers, data=data)
print(response.text)
