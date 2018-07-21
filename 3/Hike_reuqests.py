import requests

r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

data = {
    'name': 'germey',
    'age': 22
}

url = 'http://httpbin.org/get'
r = requests.get(url, params=data)
# print(r.text)
# print(r.json())
# print(type(r))

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
# print(r.text)
# print(r.content)
with open('github.ico', 'wb') as f_w:
    f_w.write(r.content)

headers = {
    'User-Agent': 'shabi'
}
url = 'https://www.zhihu.com/explore'

r = requests.get(url=url, headers=headers)
# print(r.text)

headers = {
    'Cookie': 'd_c0="AHBn00pm2g2PTgtfGYI0a_v1sk9hoEdjCT4=|1530774847"; q_c1=e3dec9c880fd43f58588ee52e2846dcf|1530774847000|1530774847000; _zap=4f873533-acc5-4750-b65c-9a86f3f534a4; _xsrf=iKkNBhLBFHZtJBoHYsISC58EPi2Ns6gt; l_n_c=1; l_cap_id="ZjhkNzJiM2MxOTM0NGU3NjgzYzFkM2ZiYTliNDU2M2U=|1532139488|d507081bbd90e15456c7b490f244410f0c1edc48"; r_cap_id="NDIwNDJkNzg4MDk0NGI0OWE0YjJhZmExYzQ4MjJkNjE=|1532139488|e241b87018caa69eddacd3966d0cde925118e11f"; cap_id="MmNkYmM1MzhjNzQ5NDQ3ZmIwMzNhMzQwODIxNDMzMjg=|1532139488|a030e603824c56e1dbcbf238224dd2f268394c66"; n_c=1; __utma=51854390.297038909.1532139492.1532139492.1532139492.1; __utmb=51854390.0.10.1532139492; __utmc=51854390; __utmz=51854390.1532139492.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=61066e97b5b7b3b0daad1bff47134a22; capsion_ticket="2|1:0|10:1532141133|14:capsion_ticket|44:ZjY4MGRlNmVkMWJlNGEyNjhjZjY3M2FmYzVjNWRiMDQ=|6b4e20d821a62f98ee9d8a9ccc36680a62fd1d8e159895a9af0d80abc08c358e"; z_c0="2|1:0|10:1532141139|4:z_c0|92:Mi4xV3Qwd0FnQUFBQUFBY0dmVFNtYmFEU1lBQUFCZ0FsVk5VLXdfWEFEd1NSTTd5YzJEejBBbUNnc05xSzlPcEd1MFFn|5aab1de8580848879a5dbb4c41f9637d4d06ae15aa40a10246fdc0a519c5ceb2"; __utmv=51854390.100-1|2=registration_date=20151015=1^3=entry_date=20151015=1',
    'Host': 'www.zhihu.com',
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

url = "https://www.zhihu.com"

r = requests.get(url=url, headers=headers)
# print(r.text)

#12306证书问题

r = requests.get('http://www.12306.cn', verify = False)
print(r.status_code)
#print(r.text)

# 代理设置

proxies = {
    'http': '60.177.226.155:18118',
    'https': '60.177.226.155:18118'
}

print(requests.get('https://www.taobao.com').status_code)

# Prepared Request
from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name': 'Germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)


