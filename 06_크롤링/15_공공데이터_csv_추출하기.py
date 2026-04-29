# 공공데이터포털 CSV 파일 데이터 추출 실습
# https://www.data.go.kr 에서 회원가입 없이 다운로드 가능한 CSV 파일 사용
# 예시: 서울시 공공도서관 현황 또는 전국 약국 현황 등 아무 CSV 파일이나 가능

import pandas as pd

# =============================================
# 실습 전 준비
# 1. https://www.data.go.kr 접속
# 2. 검색창에 "서울시 공공도서관" 또는 원하는 키워드 검색
# 3. 파일데이터 탭 → CSV 파일 다운로드 (로그인 불필요)
# 4. 다운로드한 CSV 파일을 이 .py 파일과 같은 폴더에 넣기
# =============================================


def csv_기본정보_확인():
    df=pd.read_csv("서울시 공공도서관 현황정보.csv", encoding="cp949")

    print("=== 앞 5줄 ===")
    print(df.head(5))

    print("=== 뒤 5줄 ===")
    print(df.tail(5))

    print("=== 전체 행 개수 ===")
    print(len(df))

    print("=== 열 이름 목록 ===")
    print(df.columns)

    print("=== 전체 행/열 크기 ===")
    print(df.shape)


def 특정열_추출_후_csv_저장():
    df = pd.read_csv("서울시 공공도서관 현황정보.csv", encoding="cp949")

    print("열 이름 확인:", df.columns)

    원하는열 = ["도서관명"]

    추출df = df[원하는열]

    print(추출df)

    df = pd.DataFrame(추출df)
    df.to_csv("공공데이터_추출결과.csv", index=False, encoding="utf-8-sig")
    print("공공데이터_추출결과.csv 저장 완료")

csv_기본정보_확인()
특정열_추출_후_csv_저장()