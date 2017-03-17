#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_str = "http://pythonscraping.com/pages/page1.html"
user_input = input("Enter URL : ")
if user_input != "":
	url_str = user_input

if "http://" not in url_str:
	url_str = "http://" + url_str

print("open " + url_str)
html = urlopen(url_str)
bsObj = BeautifulSoup(html.read());
print(bsObj.h1)
print("-----------------------------")
print(bsObj.head)

