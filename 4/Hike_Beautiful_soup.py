from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'xml')
print(soup.p.string)