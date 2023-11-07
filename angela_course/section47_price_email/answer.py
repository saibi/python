import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Apple-MacBook-13-inch-Storage-English/dp/B0CB745VMN/ref=sr_1_2?qid=1699325648&refinements=p_89%3AApple&rnid=2528832011&s=computers-intl-ship&sr=1-2"
# URL = "https://www.amazon.com/-/es/Western-Digital-Unidad-estado-interna/dp/B09HKGGPLR/ref=sr_1_4?crid=2QONRDDEH2E3H&keywords=ssd%2Bm.2%2B250gb&qid=1681952484&sprefix=ssd%2Bm.2%2B25%2Caps%2C101&sr=8-4&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7",
    'referer': 'https://www.amazon.com/'}

r = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.prettify())

price = float(soup.find(class_="a-price-whole").getText())
currency = soup.find(class_="a-price-symbol").getText()
print(price)
print(currency)
