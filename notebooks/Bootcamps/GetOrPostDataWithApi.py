import requests
import pandas as pd


#%% GET
GetMyApiLinkUrl="https://jsonplaceholder.typicode.com/posts"

responseGet=requests.get(GetMyApiLinkUrl,timeout=10)

if(responseGet.status_code==200):
    print("Get Bağlantı başarılı")
    response_data=responseGet.json()
    response_data_seri=pd.json_normalize(response_data)
else :
    print("Bağlantı başarısız")
#%%  Post

MyPostDic={
    "UserId":1,
    "Id":1,
    "Title":"fkkafmkas",
    "body":"kfdmskpfgmskf"
    }
PostMyApiUrl="https://jsonplaceholder.typicode.com/posts"
responsePost=requests.post(PostMyApiUrl, timeout=10,json=MyPostDic)

if(responsePost.status_code==201):
    print("Post Bağlantı Başarrılı")

else :
    print("bağlantı başarısız hata kodu",responsePost.status_code)