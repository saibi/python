from bs4 import BeautifulSoup


def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


contents = read_file('website.html')
# print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title.string)
# print(soup.a)

all_anchor_tags = soup.find_all(name="a")
print(len(all_anchor_tags))

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select(selector="#hahaha")
print(name)
