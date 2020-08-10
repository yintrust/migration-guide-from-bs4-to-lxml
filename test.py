html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from lxml import etree, html
ehtml = etree.HTML(html_doc)
a = ehtml.xpath('//a[@class="sister"]')[0]
a.set('href', '赵浩然')
b = etree.tostring(ehtml)
print(type(b))

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for sub in soup.find_all(class_='sister'):
    print(sub.extract())
print('55555555555555555555555555555555555555555555555555')
print(soup)
