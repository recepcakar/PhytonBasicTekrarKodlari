#%% İNNER LEFT RİGHT FULL JOİN 
import pandas as pd
import numpy as np

df_Ogrenciler=pd.DataFrame({
    "Ad":["Selin","Mehmet","Ali","Zeynep"],
    "DersId":[1,2,6,4]
    })
df_Dersler=pd.DataFrame({
   "DersAdi":["Matematik","Fen","Edebiyat","Tarih" ,"inkilap"],
   "DersId":[1,2,3,4,5]
    })

#inner 
MergeInner=pd.merge(df_Ogrenciler, df_Dersler,how="inner",on="DersId") #ortak olanı aldık 

#Left join
MergeLeft=pd.merge(df_Ogrenciler, df_Dersler,on="DersId",how="left")

#right join
MergeRight=pd.merge(df_Ogrenciler, df_Dersler,on="DersId",how="right")

#full join
MergeFull=pd.merge(df_Ogrenciler, df_Dersler,on="DersId",how="outer")



#CONCAT join gibi kurala göre gelmez direkt birleştirir !!!!

df1=pd.DataFrame({"Sira":[1,2,3]})
df2=pd.DataFrame({"Sira":[4,5,6]})
pd.concat([df1,df2],axis=0,ignore_index=True) #axis 0 dikeyde birleştir
pd.concat([df1,df2],axis=1,ignore_index=True)





#%% Farklı formatlarda Veri okuma 
import pandas as pd
DataFrameAsCsv=pd.read_csv("data\\CsvDataTitanic.csv",sep=",",header=0,usecols=["PassengerId","Sex","Survived","Age" ])

#header => başlığın kaçınca satırda olduğunu belirtiriz
#sep => veriler hangi karakter ile ayrıldı ?
#usecols => kullanıcağımız sütunları sçeeriz


DataFrameAsExel=pd.read_excel("data\\ExelDonusum.xlsx")
DataFrameAsExel.drop("ToplamTutar",axis=1,inplace=True)

DataFrameAsExel["Fiyat"].fillna(DataFrameAsExel["Fiyat"].mean(),inplace=True)
DataFrameAsExel["Adet"].fillna(DataFrameAsExel["Adet"].mean(),inplace=True)

DataFrameAsExel["ToplamTutar"]=DataFrameAsExel["Fiyat"]*DataFrameAsExel["Adet"]


#toplam tutarı 200den büyük olanları filtrelemek istiyorum 


NewDf1=DataFrameAsExel[DataFrameAsExel["ToplamTutar"]>200].copy() #eğer copy demezsem newdf1i her değiştirdiğimde eski veri de değişicek


#işlemlerimiiz yaptık en sona kalan verimizi bir exel ya da csv formatına dönüştürmek istersek ;

NewDf1.to_excel("data\\NewDf1.xlsx",index=False)  #oluştuuuuu


DataFrameAsCsv.to_csv("data\\Deneme.csv",sep=";") #bu da oldu .
























