import json
import requests
import json
from bs4 import BeautifulSoup
import os
from json.decoder import JSONDecodeError

base_url='https://bg.annapurnapost.com/api/search?title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE&page='



headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.5',
    }
datas=[]
datass=[]
i=0
trycount=0
exceptcount=0
while i<31:
    with open('data.json','r') as file:
        try:
            saveddata = json.load(file)
            a=len(saveddata)
            trycount=1
            print('length of json file has become ', a)
        except JSONDecodeError:
            exceptcount=1
            a=0
            pass
    
    if a<30:
        i=a+1
        final_url=base_url+str(i)
        r=requests.get(final_url, headers = headers)
        kantipursite=BeautifulSoup(r.content,'html.parser').text
        kantipursite=json.loads(kantipursite)
        kantipursite=kantipursite['data']['items']
        for j in kantipursite:
             data={
                    'page':i,
                    'info':j
                    }
        saveddata.append(data)


        with open("data.json", "w") as outfile:
            json.dump(saveddata, outfile,indent=4)
            print('The data updated of ',i)
            
    i=i+1  
   
          