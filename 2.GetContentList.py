import requests
import re
from bs4 import BeautifulSoup

r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = BeautifulSoup(r.text, "lxml")

#1
p = soup.findAll("div", class_="col-md-4 col-xl-4 col-lg-4")
for index, element in enumerate(p):
    caption = element.find("div", class_="caption" )
    name= caption.a.string #Give name
    price=caption.h4.string #Give price
    description=caption.p.string #Give description
    titleAttribute = caption.a.get("title") #Give value of attribute => title
    print("Product Name: "+ name) 
    print("Product Price: "+ price)
    print("Product Description: "+ description)
    print("Value from attribute: "+ titleAttribute)
    print("______________________________________") 
    print()


#2
#Print all p a div tags
print()
print("#3: Print all p a div tags")
selectedTags = soup.findAll(["p","a","div"])
print(selectedTags) 

#3
#Print string, But this will exact match the string
print()
print("#3: Print string, But this will exact match the string")
searchedString = soup.findAll(string="E-commerce training site")
print(searchedString) 

#4
#Print string using regex (re) whcich will return all the string containg that string, not exact match
print()
print("#4: Print string using regex (re) whcich will return all the string containg that string, not exact match") 
expression = soup.findAll(string=re.compile("E-commerce"))
print(expression) 