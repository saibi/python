#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except (HTTPError,URLError) as e:
		print(e)
		return None
	try:
	 	bsObj = BeautifulSoup(html.read())
	 	title = bsObj.body.h1
	except AttributeError as e:
		print(e)
		return None
	return title


url_str = "http://pythonscraping.com/pages/page1.html"
user_input = input("Enter URL : ")
if user_input != "":
	url_str = user_input

if "http://" not in url_str:
	url_str = "http://" + url_str

print("open " + url_str)

title = getTitle(url_str)

if title is None:
	print("Title could no be found")
else:
	print(title)

