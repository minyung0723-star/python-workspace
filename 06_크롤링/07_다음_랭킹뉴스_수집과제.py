import requests
import newspaper
from bs4 import BeautifulSoup
import time

# 브라우저인 척 하는 헤더 (없으면 차단당할 수 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

# ① 다음 랭킹 뉴스 페이지에서 URL 20개 가져오기
def url목록가져오기():
    랭킹주소 = "https://entertain.daum.net/ranking/popular"

    res = requests.get(랭킹주소, headers=headers)

    soup = BeautifulSoup(res.text,"html.parser")

    랭크목록 = []
    태그들 = soup.select("a.link_thumb")

    for 태그 in 태그들[:20]:  # 최대 20개
        링크 = 태그.get("href")
        if 링크 and "article" in 링크:
            if 링크.startswith("/"):
                링크 = "https://news.daum.net" + 링크
            if 링크 not in 랭크목록:
                랭크목록.append(링크)
        if len(랭크목록) >= 20:
            break

    print(f"총 {len(랭크목록)}개 URL 수집 완료!")
    return 랭크목록


# ② 기사 URL 1개로 제목 / 내용 / 기자 / 날짜 수집
def 기사수집(url):

    아티클 = newspaper.article(url, language="ko")

    아티클.parse()

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    기자태그 = soup.find("span", class_="txt_info")

    날짜태그 = soup.find("span", class_="num_date")

    제목 = 아티클.title
    내용 = 아티클.text[:100] + "..."   # 내용은 100자만
    기자 = 기자태그.text.strip() if 기자태그 else "못 찾음"
    날짜 = 날짜태그.text.strip() if 날짜태그 else "못 찾음"

    return 제목, 내용, 기자, 날짜


# ③ 전체 실행 함수
def 뉴스20개수집():

    url목록 = url목록가져오기()

    for i, url in enumerate(url목록):
        print(f"\n[ {i+1}번째 기사 ]")

        제목, 내용, 기자, 날짜 = 기사수집(url)

        print("제목 :", 제목)
        print("기자 :", 기자)
        print("날짜 :", 날짜)
        print("내용 :", 내용)
        time.sleep(2)
    print("\n수집 완료")


# 실행
뉴스20개수집()