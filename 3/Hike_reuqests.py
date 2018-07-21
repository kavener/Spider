import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

data = {
    'name': 'germey',
    'age': 22
}

url = 'http://httpbin.org/get'
r = requests.get(url, params=data)
print(r.text)
print(r.json())
print(type(r))

# 知乎为例
# import re
#
# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
# }
#
# r = requests.get(url=url, headers=headers)
#
# pattern = re.compile('question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# 获取github图标

url = 'https://github.com/favicon.ico'
r = requests.get(url=url)
print(r.text)
print(r.content)
with open('github.ico', 'wb') as f_w:
    f_w.write(r.content)
