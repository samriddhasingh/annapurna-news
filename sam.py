import requests
import json
from bs4 import BeautifulSoup
import os

base_url1='https://bg.annapurnapost.com/api/search?title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE'
base_url2='https://bg.annapurnapost.com/api/search?title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE&page=2'
base_url3='https://bg.annapurnapost.com/api/search?title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE&page=33'


headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.5',
    }

r=requests.get(base_url1, headers = headers)
s=requests.get(base_url2, headers = headers)
p=requests.get(base_url3, headers = headers)
kantipursite=BeautifulSoup(r.content,'html.parser').text
kantipursite2=BeautifulSoup(s.content,'html.parser').text
kantipursite3=BeautifulSoup(s.content,'html.parser').text
kantipursite=json.loads(kantipursite)
kantipursite2=json.loads(kantipursite2)
kantipursite3=json.loads(kantipursite3)
kantipursite=kantipursite['data']['items']
kantipursite2=kantipursite2['data']['items']
kantipursite3=kantipursite3['data']['items']


for i in kantipursite2:
    kantipursite.append(i)
for i in kantipursite3:
    kantipursite.append(i)
datas=[]

for i in range(1,4):
    count=0
    for j in kantipursite:
        count=count+1
        if count > 10:
            break
        data={
            'page':i,
            'details':j
        }
    datas.append(data)

with open("data.json", "w") as outfile:
    json.dump(datas, outfile)



