from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
#
# a_finder = soup.find_all("a")
# print(a_finder)
#
# head_tag = soup.head
# children = head_tag.contents
# for child in head_tag.children:
#     print(child)
# last_a_tag = soup.find("a", id="link3")
# for element in last_a_tag.next_elements:
#     print(element)

finder = soup.find_all(id=True)
# soup.prettify(finder)
print(finder)


parent = head_tag.parent
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
sibling = sibling_soup.b.next_sibling

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
type(tag)


soup = BeautifulSoup(html_doc, 'html.parser')
b = soup.b
p = soup.p
a = soup.a
i = soup.i
title = soup.title
head = soup.head

tag.name = "spoon"

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
a = tag['id']

b = tag.attrs

doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)

pass