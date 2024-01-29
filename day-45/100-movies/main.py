import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
headings = soup.select(selector="[data-test^=listicle-item] h3")
titles = [heading.getText() for heading in headings[::-1]]

with open("top-movies.txt", "w") as data_file:
    for title in titles:
        data_file.write(f"{title}\n")