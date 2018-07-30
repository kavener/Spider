import requests
import re
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

pattern = re.compile(
    'class="board-index.*?>(.*?)</i>.*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="score"><.*?>(.*?)<.*?class="fraction">(.*?)</i>',
    re.S)


def get_info(url):
    return requests.get(url=url, headers=headers).text


def make_url(offset):
    return 'http://maoyan.com/board/4?offset=' + str(offset)


def get_movie_info(html):
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'ranking': item[0],
            'film_name': item[1],
            'To_star': item[2].strip()[3:],
            'Release_time': item[3],
            'score': item[4] + item[5]
        }


def save_info(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = make_url(offset)
    html = get_info(url)
    for item in get_movie_info(html):
        print(item)
        save_info(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
