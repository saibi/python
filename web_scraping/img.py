#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
	print(image["src"])


mytags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for t in mytags:
    print(t)
