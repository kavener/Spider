import urllib.request
import urllib.parse
import urllib.error
import socket

response = urllib.request.urlopen('https://www.python.org')
print(type(response))
print(response.status)
print(response.getheaders())

# data参数
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

# timeout参数
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e :
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 使用Request配置参数
request = urllib.request.Request('https://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'Germey'
}

data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
