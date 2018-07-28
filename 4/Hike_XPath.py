from lxml import etree
import requests
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html>first item</a></li>
<li class="item-1"><a href="link2.html>second item</a></li>
<li class="item-inactive"><a href="link3.html>first item</a></li>
<li class="item-1"><a href="link1.html>fourth item</a></li>
<li class="item-0"><a href="link1.html>fifth item</a>
</ul>
</div>
'''

# html = requests.get("https://www.python.org").text
# print(html)
chang_html = etree.HTML(text)
result = etree.tostring(chang_html)
print(result.decode("utf-8"))
# print(type(result))
# with open('python_org.html', 'w') as f:
#     f.write(html)
# html = etree.parse('python_org.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)
