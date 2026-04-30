import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 설정 2줄을 작성하시오. (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("경찰청_범죄 발생 지역별 통계_20241231.csv", encoding="cp949")

def 막대그래프():
    # 강력범죄만 필터링
    df_강력 = df[df['범죄대분류'] == '강력범죄']

    plt.bar(df_강력['범죄중분류'], df_강력['서울 강남구'])  # TODO: x축 범죄중분류, y축 서울 강남구
    plt.title("강력범죄 종류별 서울 강남구 발생 건수")                         # TODO: 적절한 제목 작성
    plt.xlabel("범죄명")
    plt.ylabel("범죄수")
    plt.xticks(rotation=45)              # TODO: X축 글자 겹치지 않게 기울이기
    plt.tight_layout()
    plt.show()
# 막대그래프()

def 파이차트():
    df_강력 = df[df['범죄대분류'] == '강력범죄']

    plt.pie(
        df_강력['서울 강남구'],         # TODO: 서울 강남구 수치 컬럼
    labels=df_강력['범죄중분류'],  # TODO: 범죄중분류 컬럼
    autopct="%1.1f%%")       # TODO: 퍼센트 소수점 1자리 표시
    plt.title("강력범죄 종류별 비율")
    plt.show()
# 파이차트()

def 가로막대그래프():
    plt.barh(df['범죄중분류'], df['서울 강남구'], label='서울')  # TODO: y축 범죄중분류, x축 서울 강남구
    plt.barh(df['범죄중분류'], df['부산 중구'], label='부산')  # TODO: y축 범죄중분류, x축 부산 중구
    plt.title("범죄 종류별 서울 강남구 vs 부산 중구 비교")
    plt.xlabel("범죄수")
    plt.legend()       # 범례 표시
    plt.tight_layout()
    plt.show()
# 가로막대그래프()

def 히스토그램():
    plt.hist(df['서울 강남구'], bins=10)  # TODO: 서울 강남구 컬럼, 구간 10개
    plt.title("서울 강남구 범죄 건수 분포")
    plt.xlabel("범죄 건수")
    plt.ylabel("빈도")
    plt.show()
# 히스토그램()

def 산점도():
    plt.scatter(df['서울 강남구'], df['서울 서초구'], alpha=0.7)
    # TODO: x축 서울 강남구, y축 서울 서초구, 투명도 0.7
    plt.title("서울 강남구 vs 서울 서초구 범죄 상관관계")
    plt.xlabel("강남구 범죄건수")
    plt.ylabel("서초구 범죄건수")
    plt.show()
# 산점도()

def 그래프이미지로저장():
    df_강력 = df[df['범죄대분류'] == '강력범죄']

    plt.bar(df_강력['범죄중분류'], df_강력['서울 강남구'])
    plt.title("강남구 강력범죄 현황")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("강남구_강력범죄.png")    # TODO: "강남구_강력범죄.png" 로 저장하시오.
    plt.show()
그래프이미지로저장()