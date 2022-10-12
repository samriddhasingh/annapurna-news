import json
import requests


base_url='https://bg.annapurnapost.com/api/search?title=%E0%A4%95%E0%A5%8B%E0%A4%B0%E0%A5%8B%E0%A4%A8%E0%A4%BE&page='



headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.95 Safari/537.36',
        'Accept-Language': 'en-GB,en;q=0.5',
    }


def main():
    with open('samriddha.json','r') as file:
        try:
            saveddata = json.load(file)
            print('length of json file has become ', a)
        except :
            saveddata=[]
    a=len(saveddata)

    while True:
        if a<10:
            pagenumber= int(a/10)+1
            final_url=base_url+str(pagenumber)
            print(final_url)
            r=requests.get(final_url, headers = headers)
            # kantipursite=BeautifulSoup(r.content,'html.parser').text
            kantipursite=json.loads(r.text)
            print(len(kantipursite['data']['items']))
            for i in range(len(kantipursite['data']['items'])):
                title = kantipursite['data']['items'][i]['title']
                content = kantipursite['data']['items'][i]['content']
                saveddata.append({"title": title})
            a =a +10
            with open("samriddha.json", "w") as outfile:
                json.dump(saveddata, outfile,indent=4)
        else:
            print("Finished")
            break

if __name__ =='__main__':
    main()