import openpyxl
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup as bs
import time
from lxml import html

data=pd.read_csv("C:/Users/jai/Desktop/jay.csv")

country=data["country"]
asin=data["Asin"]

url=f"https://www.amazon.{country[0]}/dp/{asin[0]}"

title=[]
image_url=[]
price=[]
product_details=[]
i=0


start_time=time.time()
while i<1000:
    page_html=requests.get(url)
    #tree=html.fromstring(page_html.content)

    if(page_html.ok==False):
        print("url showing error",url)
        continue
    
    #print(page_html.ok)
    page_soup=bs(page_html.content,"html.parser")
    data_for_all=page_soup.findAll('div',class_="a-section a-spacing-base")
    print("data:" ,data_for_all)
    

    i+=1
    url=f"https://www.amazon.{country[i]}/dp/{asin[i]}"

end_time=time.time()
print("The difference time between start and end time : ",(end_time-start_time))
