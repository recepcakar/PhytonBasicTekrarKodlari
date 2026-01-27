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






#%%