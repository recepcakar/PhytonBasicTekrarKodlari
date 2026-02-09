import requests
import pandas as pd
import numpy as np
url = "https://youtube-transcript3.p.rapidapi.com/api/transcript"

querystring = {"videoId":"S9bCLPwzSC0"} #video id veriyorum

headers = {
	"x-rapidapi-key": "",
	"x-rapidapi-host": "youtube-transcript3.p.rapidapi.com"
}

responseForEminem = requests.get(url, headers=headers, params=querystring)
if(responseForEminem.status_code==200):
    dataForEminem=responseForEminem.json()
    transcriptForEminem = dataForEminem.get("transcript")
    
    if transcriptForEminem:
        dfForEminem = pd.DataFrame(transcriptForEminem)
        dfForEminem["duration"] = dfForEminem["duration"].astype(float) #float yaptım ki sonradan toplaması kolay olsun
        dfForEminem.to_excel("transcriptForEminem.xlsx", index=False)
        print("Excel dosyası oluşturuldu")
    else:
        print("Transcript boş veya kapalı")


url = "https://youtube-transcript3.p.rapidapi.com/api/transcript"

querystring = {"videoId":"PBZfCmlRIVs"} #video id veriyorum

headers = {
	"x-rapidapi-key": "",
	"x-rapidapi-host": "youtube-transcript3.p.rapidapi.com"
}

responseForPassenger = requests.get(url, headers=headers, params=querystring)
if(responseForPassenger.status_code==200):
    dataForPassenger=responseForPassenger.json()
    transcriptForPassenger = dataForPassenger.get("transcript")
    
    if transcriptForPassenger:
        dfForPassenger= pd.DataFrame(transcriptForPassenger)
        dfForPassenger["duration"] = dfForPassenger["duration"].astype(float) #float yaptım ki sonradan toplaması kolay olsun
        dfForPassenger.to_excel("transcriptForPassenger.xlsx", index=False)
        print("Excel dosyası oluşturuldu")
    else:
        print("Transcript boş veya kapalı")
# eminem şarkıyı ne kadar hızlı söyler?




#passenger [Music] ve [applause] yazan satırları çıkarıcaz
#Toplam harf sayısını süreye bölücez
#çıkan harf/saniye oranı ile emineminkini kıyaslıocağız






dfForPassengerReal=dfForPassenger.loc[dfForPassenger["text"]!="[Music]"]
dfForPassengerReal=dfForPassengerReal.loc[dfForPassengerReal["text"]!="[Applause]"]


duration_passenger=dfForPassengerReal.duration.sum() #passenger konuşma süresi
duration_eminem=dfForEminem.duration.sum()  #eminem konuşma süresi


#passenger kaç harf var ?
total_passenger=0
for i in dfForPassengerReal["text"].dropna():
    total_passenger+=len(i)


total_eminem=0
for i in dfForEminem["text"].dropna():
    total_eminem+=len(i)






ratio_eminem=total_eminem/duration_eminem
ratio_passenger=total_passenger/duration_passenger



yazılacak_yazı="passenger" if ratio_passenger>ratio_eminem else     "Eminem"

print(yazılacak_yazı,"çok daha hızlı konuşuyor ")







