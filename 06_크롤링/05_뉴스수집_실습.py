import requests
import newspaper
from bs4 import  BeautifulSoup

url="https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

def 방법1번():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("h2", id="title_area")
    print("제목 : ", title.text.strip() if title else "못찾음")
    content = soup.find("article", id="dic_area")
    print("내용 : ", content.text.strip() if content else "못찾음")
    reporter = soup.find("span", class_="byline_s")
    print("기자 : ", reporter.text if reporter else "못찾음")

# 방법1번()

def 방법2번():

    article = newspaper.article(url, language = "ko")
    article.parse()

    print("제목 : ",article.title)
    print("내용 : ",article.text)
    print("기자 : ",article.authors)
    print("날짜 : ",article.publish_date)

# 방법2번()