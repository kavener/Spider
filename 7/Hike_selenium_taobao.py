from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support .wait import WebDriverWait
from urllib.parse import quote
import time
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 100)
KEYWROD = 'ipad'
def index_page(page):
    url = 'https://s.taobao.com/search?q=' + quote(KEYWROD)
    browser.get(url)
    if page > 15:
        # time.sleep(3)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
        input.clear()
        input.send_keys(page)
        input.send_keys(Keys.ENTER)

for i in range(1,30):
    index_page(i)

def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-')