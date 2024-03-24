import requests
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

# printing r is important to check whether the website allow us to scrap data or not
# print(r)

soup=BeautifulSoup(r.text,"lxml")

p = soup.find("div",class_="jumbotron").h1.string
print(p)