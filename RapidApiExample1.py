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
