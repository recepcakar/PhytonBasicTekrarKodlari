# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 14:03:28 2026

@author: rrece
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd



TumSozlerList=[]
TumYazarlarList=[]
url="https://quotes.toscrape.com/page/"
 
for i in range(1,10):
    NewUrl = f"{url}{i}/"
    response=requests.get(NewUrl, timeout=10)
    if(response.status_code==200):
        soup=BeautifulSoup(response.content,"html.parser")
        divTagForPage=soup.find_all("div",class_="quote") #classı quoter olanları oku
        for div in divTagForPage:
             
            soz=div.find("span",class_="text").text
            TumSozlerList.append(soz)
             
            yazar=div.find("small",class_="author").text
            TumYazarlarList.append(yazar)


Dic1={
      "Yazar":TumYazarlarList,
      "Soz":TumSozlerList
      }
#iki boyutlu liste tanımlayıp da yapabilirdik 

"""
veriliste.appen({"yazar".yazar,"soz".soz})

    
"""
dfPage1=pd.DataFrame(data=Dic1)