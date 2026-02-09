# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 10:03:57 2026
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
url ="https://quotes.toscrape.com/"

response=requests.get(url, timeout=10) #html kodları döndü 

# response.json()  api beni blokladı bu yzden web scrape yapıcağım

if(response.status_code==200):
    soup=BeautifulSoup(response.content,"html.parser")
    ilkh1tag=soup.find(name="h1")
    ilkh1tag.text#içerisindeki text
    ilkh1tag.find("a") #içerisindeki a etiketi
    ilkh1tag.find("a")["style"]  #ama böyle sadece bulduğu ilkleri gösterir 
    
    #tekrar tekrar istiyorsak for döngüsüne girmeliyiz
    SozlerList=[]
    YazarlarList=[]
    divTags=soup.find_all("div",class_="quote") #classı quoter olanları oku
    for div in divTags:
        
        soz=div.find("span",class_="text").text
        SozlerList.append(soz)
        
        yazar=div.find("small",class_="author").text
        YazarlarList.append(yazar)
        

else :
    print("siteye erişemedik")
    



Dic1={
      "Yazar":YazarlarList,
      "Soz":SozlerList
      }
#iki boyutlu liste tanımlayıp da yapabilirdik 

"""
veriliste.appen({"yazar".yazar,"soz".soz})

    
"""
dfPage1=pd.DataFrame(data=Dic1)

#artık temiz bir veriye çevirdik.



#peki neden bütün söz ve yazarı 1 sayfaya almadı ?
#eğer tüm veriyi aynı anda sayfaya çekmek istersek
"""
veri çoksa

işlem uzun sürer

kullanıcı bekler

"""

#sonraki sayfadaki verileri okumak için page 1 2 3 4 5 istek atmalıyım























