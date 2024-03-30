from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.iplt20.com/stats/2024")
# Wait for the table to load (you may need to adjust the time)
driver.implicitly_wait(10)
html = driver.page_source
driver.close()
soup = BeautifulSoup(html, "lxml")
table = soup.find("table", class_="st-table statsTable ng-scope")
headers =  table.findAll("th")

headerList=[]
for header in headers:
    headerList.append(header.text)

dataframe = pd.DataFrame(columns=headerList)
print(dataframe)

rows = table.findAll("tr")
for row in rows[1:]:
    dataInRow = row.findAll("td")
    row=[tr.text for tr in dataInRow]
    l = len(dataframe)
    dataframe.loc[l] = row 

    # for data in dataInRow:
    #     l = len(dataframe)
    #     dataframe.loc[l] = data.text 

dataframe.to_excel("./5.matchStates.xlsx")
print(dataframe)

