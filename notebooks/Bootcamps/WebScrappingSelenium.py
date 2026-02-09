#bir web sitesine sürekli istek atmak banlanmamıza neden olabilir webscrapinge dikkat! 
#bunun için time kütüphanesini kullanıp yavaş yavaş istek atmamız gerekir
"""
import time
time.sleep(10)
"""

# İBB duyurular bölümüyle çalışacağız.
# Sayfa değiştirildiğinde URL değişmiyor çünkü sayfa tamamen yenilenmiyor.
# Sunucu (.NET / Java vb.) veriyi API üzerinden gönderiyor,
# tarayıcı tarafındaki JavaScript bu veriyi AJAX (fetch) ile sonradan alıyor.
# Böylece sadece içerik güncelleniyor, sayfa baştan yüklenmediği için kullanıcıya daha hızlı görünüyor.


"""
Önceki örnekte, sayfa geçişleri URL üzerinden yapıldığı için
doğrudan URL’i bildiğimizden erişebiliyorduk.

Bu senaryoda ise sayfa geçişleri bir butona tıklanarak yapılıyor
ve URL değişmiyor. Bu yüzden tarayıcıda butona tıklanmış gibi
davranmamız gerekiyor.

Bu davranışı taklit edebilmek için Selenium kullanacağız.
Selenium, gerçek bir tarayıcıyı kontrol ettiği için
buton tıklama, pop-up kapatma gibi kullanıcı etkileşimlerini
simüle edebilir.
"""

#%% Seleniuma yarın geçiceğim bu yüzden şimdilik tekrar amaçlı bir örnek yapayım
#oluşturma 09.02.2026
import requests
from bs4 import BeautifulSoup
ibb_url="https://ibb.istanbul/gundem/duyurular"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

response_ibb=requests.get(ibb_url, headers=headers)
list1=[]
if response_ibb.status_code==200:
    soup=BeautifulSoup(response_ibb.content,"html.parser")
    div=soup.find("div",class_="grid gap-x-5 gap-y-5")
    div.find("a").text
 #yapılmadı çünkü kaynağı görüntüle olmayan web sayfalarında request çalışmaz!!!!!
    
#%%





























