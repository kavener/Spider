from pyquery import PyQuery as pq
doc = pq(filename='python_org.html')
print(doc('li'))