import requests
from bs4 import BeautifulSoup
import lxml

import datetime as dt
from mail_test import send_mail

# amazon link
# URL = "https://www.amazon.com/Apple-MacBook-13-inch-Storage-English/dp/B0CB745VMN/ref=sr_1_2?qid=1699325648&refinements=p_89%3AApple&rnid=2528832011&s=computers-intl-ship&sr=1-2"

# gmarket link
URL = "https://item.gmarket.co.kr/Item?goodscode=2507383344"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    # 'referer': 'https://www.amazon.com/', # for amazon
}

response = requests.get(URL, headers=headers)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
price_text = soup.select(".price_innerwrap-coupon > .price_real")[0].get_text()
price = int(price_text.replace(",", "").replace("원", ""))
print(price)

if price < 2000000:
    print("Buy!")
    now = dt.datetime.now()
    send_mail(to_email="kimyoungmin@gmail.com",
              subject=f"Price:{now}", message=f"Price: {price}")
