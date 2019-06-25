from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://ekiss.huvitz.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)
print(bsObject.head.title)

for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))
