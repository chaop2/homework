from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#랭크
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#노래제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#가사
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

infos = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for info in infos:
    rank = info.select_one('td.number').text[0:5].strip()
    song = info.select_one('td.info > a.title.ellipsis').text.strip()
    singer = info.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, song, singer)
    doc = {
        'rank' : rank,
        'song' : song,
        'singer' : singer }
    db.genie_rank.insert(doc)


