#!/usr/bin/env python3

from urllib.request import urlopen

url = input("Enter URL : ")
if url == "" :
	url = "http://pythonscraping.com/pages/page1.html"

if "http://" not in url :
	url = "http://" + url

html = urlopen(url)
print(html.read())
