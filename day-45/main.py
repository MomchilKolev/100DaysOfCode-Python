from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [score.getText().split()[0] for score in soup.select(selector=".score")]
print(article_upvotes)
print(max(list(map(int, article_upvotes))))
highest_upvote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote_index], article_links[highest_upvote_index])

# with open("website.html") as data_file:
#     contents = data_file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.a)
#
# # print(soup.find_all(name="p"))
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(selector=".heading")
# print(headings)

