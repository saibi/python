import requests
from bs4 import BeautifulSoup


BILLBOARD_END_POINT = "https://www.billboard.com/charts/hot-100"

# travel_date = input(
#     'Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
travel_date = "2023-10-04"

url = f"{BILLBOARD_END_POINT}/{travel_date}"
print(url)

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs = [tag.getText().strip() for tag in soup.select(
    selector="li.o-chart-results-list__item > h3#title-of-a-story.c-title")]
singers = [tag.getText().strip() for tag in soup.select(
    selector="li.o-chart-results-list__item > h3#title-of-a-story + span.c-label")]

print(len(songs))
print(len(singers))

for i in range(len(songs)):
    print(f"{i+1}. {songs[i]} - {singers[i]}")
