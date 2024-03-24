import requests
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

soup=BeautifulSoup(r.text,"lxml")

p = soup.find("div",class_="jumbotron").h1.string
print(p)