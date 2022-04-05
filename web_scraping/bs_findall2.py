#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

#nameList = bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
nameList = bsObj.findAll("span", {"class":"green", "class":"red"})
for name in nameList:
	print(name)
	print(name.get_text())
	print()
