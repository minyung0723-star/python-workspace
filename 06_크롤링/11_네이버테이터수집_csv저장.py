import re

import requests
import newspaper
from bs4 import  BeautifulSoup
import pandas as pd

url="https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

def 방법1번():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("h2", id="title_area")
    content = soup.find("article", id="dic_area")
    reporter = soup.find("span", class_="byline_s")


    제목데이터 = title.text.strip() if title else "못찾음"
    내용데이터 = content.text.strip() if content else "못찾음"
    기자데이터 = reporter.text if reporter else "못찾음"



    df1= pd.DataFrame({"제목": [제목데이터],"기자": [기자데이터],"내용": [내용데이터]})
    df2= pd.DataFrame(dict(제목 = [제목데이터],기자 = [기자데이터],내용 = [내용데이터]))
    df2.to_csv("requests_naver뉴스수집.csv", index=False, encoding="utf-8-sig")
    print("requests_naver뉴스수집.csv 파일 저장 완료")

# 방법1번()

def 방법2번():

    article = newspaper.article(url, language = "ko")
    article.parse()

    제목 = article.title
    내용 = article.text
    이메일데이터 = re.findall(r'[\w.]+@[\w.]+',내용)
    기자 = 이메일데이터[0] if 이메일데이터 else "못 찾음"
    날짜 = article.publish_date

    df= pd.DataFrame({"제목": [제목],"기자": [기자],"내용": [내용]})
    df.to_csv("newspaper_naver뉴스수집.csv", index=False, encoding="utf-8-sig")
    print("저장 완료")

방법2번()