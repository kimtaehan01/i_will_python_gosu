import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
now = str(int(datetime.today().strftime("%Y%m%d"))-1) #전날 yesterday
page = '1' #링크용
check_page = '1' #비교용
datas = {} #뉴스 제목 및 링크

while(1):
    response=requests.get("https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=001&listType=title&date="f'{now}'"&page="f'{page}', headers={'User-Agent': f'{headers}'})
    html=response.text
    soup=BeautifulSoup(html,'html.parser')
    ul=soup.find("div",class_="paging")
    npage=ul.find("strong")
    print(npage.text)
    print(type(npage))
    check_page = npage.text
    if page != check_page:
        break 
    print("ok")
    news=soup.find("td",class_="content")
    for a in news.find_all("a",class_="nclicks(fls.list)"):
        title=a.text
        url = a['href']
        datas[title] = url
    page=str(int(page)+1)    

for k, v in datas.items():
    print(k,v)