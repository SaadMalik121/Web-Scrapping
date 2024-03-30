# print("EXAMPLE 1")


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# r = requests.get("https://ticker.finology.in/")

# soup=BeautifulSoup(r.text,"lxml")

# headersList=[]
# dataList=[]

# table = soup.find("table",class_="table table-sm table-hover screenertable")
# headers = table.findAll("th")

# for header in headers:
#     headersList.append(header.text)

# dataFrame = pd.DataFrame(columns=headersList)
# print(dataFrame)

# rows = table.findAll("tr")
# for i in rows[1:]: #As 1st row is header which we already extracted. So, we start from 1.
#     data=i.findAll("td")
#     row=[tr.text.strip() for tr in data]
#     l=len(dataFrame)
#     dataFrame.loc[l] = row

# print(dataFrame)



# In the above example we see that column 1 "company" contain many"/n" in their name. to remove this we can write..
print("EXAMPLE 2")

import requests
import pandas as pd
from bs4 import BeautifulSoup

r = requests.get("https://ticker.finology.in/")

soup=BeautifulSoup(r.text,"lxml")

headersList=[]
dataList=[]

table = soup.find("table",class_="table table-sm table-hover screenertable")
headers = table.findAll("th")

for header in headers:
    headersList.append(header.text)

dataFrame = pd.DataFrame(columns=headersList)
# print(dataFrame)

rows = table.findAll("tr")
for i in rows[1:]: #As 1st row is header which we already extracted. So, we start from 1.
    firstData=i.findAll("td")[0].text.strip()
    data=i.findAll("td")[1:]
    row=[tr.text.strip() for tr in data]
    row.insert(0,firstData)
    l=len(dataFrame)
    dataFrame.loc[l] = row

print(dataFrame)
