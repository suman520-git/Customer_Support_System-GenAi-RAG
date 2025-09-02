import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from os import getcwd

# headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}


product_title=[]
rating=[]
summary=[]
review=[]

for i in range(2,12):
    
    url="https://www.flipkart.com/search?q=earbuds&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_7_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=earbuds&requestId=8f28576c-d7f4-455f-8ab8-beeb6723c2d1&as-searchtext=earbuds&page="+str(i)



    r=requests.get(url)
    # print(r)
    soup=BeautifulSoup(r.text,"lxml")
    box=soup.find("div",class_="DOjaWF gdgoEp")
    
    names=box.find_all("a",class_="wjcEIp")
    for i in names:
        name=i.text
        product_title.append(name)

    ratings=box.find_all("div",class_="XQDdHH")
    for i in ratings:
        name=i.text
        rating.append(name)


    summ=box.find_all("div",class_="yN+eNk w9jEaj")
    for i in summ:
        name=i.text
        summary.append(name)

    rev=box.find_all("div",class_="K5lpE5")
    for i in rev:
        name=i.text
        review.append(name)    

df=pd.DataFrame({"product_title":product_title,"rating":rating,"summary":summary,"review":review})

path=getcwd()

df.to_csv(os.join_path(path,"data","flipkart_product_review.csv"))





