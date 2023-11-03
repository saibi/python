from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

result = soup.select(selector="h3.listicleItem_listicle-item__title__hW_Kn")

titles = [tag.getText() for tag in result]
ascending_titles = titles[::-1]
print(ascending_titles)

with open("movies.txt", mode="w") as file:
    for title in ascending_titles:
        file.write(f"{title}\n")
