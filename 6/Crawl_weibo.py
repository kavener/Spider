from urllib.parse import urlencode
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers={
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
    params = {
        'display': '0',
        'retcode': '6102',
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }

    url = base_url+urlencode(params)
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
print(get_page(1))

from pyquery import PyQuery as pq

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes')
            weibo['comments'] = item.get('comments')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

if __name__ == '__main__':
    for page in range(1,11):
        json = get_page(page)
        results = parse_page(json)
        # for result in results:
        #     print(result)