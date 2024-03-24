import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
soup = BeautifulSoup(r.text, "lxml")


titleList = []
descriptionList = []
priceList = []
reviewList = []

titles = soup.findAll("a",class_="title")
prices = soup.findAll("h4",class_="float-end price card-title pull-right")
descriptions = soup.findAll("p",class_="description card-text")
reviews = soup.findAll("p",class_="float-end review-count")

for title in titles:
    titleList.append(title.text)

for price in prices:
    priceList.append(price.text)

for review in reviews:
    reviewList.append(review.text)

for description in descriptions:
    descriptionList.append(description.text)



dataFrame = pd.DataFrame({"Product Name":titleList, "Description":descriptionList, "Price":priceList,"Reviews":reviewList})

# print(dataFrame)

# dataFrame.to_csv("product_details.csv")

dataFrame.to_excel("product_details.xlsx") #download=> pip install openpyxl



