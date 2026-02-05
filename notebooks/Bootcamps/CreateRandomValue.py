#%% random kütüphanesi keşif

import random

print(random.randrange(1,10)) #0-9 arası sayı döndürür son eleman dahil deği!
print(random.randint(1,10)) #1-10 arası sayı döndürür son eleman dahil
#random.random(0,1) #float değer seçer! 0.0 1.0 gibi

sayilar = [1, 2, 3, 4, 5]
random.shuffle(sayilar) #listenin elemanlarını karıştırır.


#%%Tutulan sayıyı tahmin etme oyun

PcSayiTut=random.randint(1, 5)
CikisYapıldimi=0
denemesayisi=0
while(not CikisYapıldimi):
    denemesayisi+=1
    Tutulan_deger=input("Tahmin et")
    if(int(Tutulan_deger)==PcSayiTut):
        print("Tebrikler Doğru sayi")
        CikisYapıldimi=1
    else:
        print("Yanlış sayi")
        

print(denemesayisi,"Denemede Buldunuz")
        
#%% Taş-Kağıt-Makas Oyunu

OynamaListesi=["taş", "kağıt", "makas"]

PcSkor=0
KullaniciSkor=0

Oynanabilir=1

while(Oynanabilir):
    Pcsecim=random.choice(OynamaListesi) #listeden random rastgele seçebilir
    kullaniciSecimIndex=int(input("Taş :0 , Kağıt :1 ,Makas 2"))
    
    PcsecimIndex=OynamaListesi.index(Pcsecim)
    sonuc=(kullaniciSecimIndex-PcsecimIndex)%3 #-1%3  ==2  buna dikkat edelim!!!
    if(sonuc==0):
        print("Berabere")
    elif(sonuc==1):
        print("Kazandın")
        KullaniciSkor+=1
    else:
        print("Pc kazandı")
        PcSkor+=1
    print("Pc tahmini:",Pcsecim)
    print("***********************************************")
    print("***********************************************")
    print("***********************************************")
    
    if(PcSkor==3 or KullaniciSkor==3):
        Oynanabilir=0

print("Pc : ",PcSkor,"\n Kullanıcı:",KullaniciSkor)    
        
    
#%%
import numpy as np
TutulanSayilarinListesi=[]
for i in range(10):
    tutulanSayi=random.randint(0, 100)
    TutulanSayilarinListesi.append(tutulanSayi)

array1=np.array(TutulanSayilarinListesi) #arraylar sabit boyut olduğundan ilk listeye ekledim sonra arraye çevirdim

print("Tutulan Sayıların ortalaması : ",array1.mean())
print("Tutulan Sayıların min : ",array1.min())
print("Tutulan Sayıların max : ",array1.max())
