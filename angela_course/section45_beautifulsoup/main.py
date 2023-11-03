from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# article_tag = soup.find(name="a", class_="storylink")
# print(article_tag.getText())

article_texts = []
article_links = []
article_upvotes = []

result = soup.select(selector="span.titleline > a")
for tag in result:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))

article_upvotes = [int(score.getText().split()[0])
                   for score in soup.select(selector="span.score")]

print(article_texts)
print(article_links)
print(article_upvotes)

index = article_upvotes.index(max(article_upvotes))
print(article_texts[index], article_upvotes[index])
