import pandas as pd
import matplotlib.pyplot as plt

# TODO: 한글 깨짐 방지 설정 2줄을 작성하시오. (윈도우 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("국토교통부_외국인 조종사 국적별 현황_20250331.csv", encoding="cp949")

def 막대그래프():
    # 항공사 컬럼만 추출 (국적 컬럼 제외)
    항공사목록 = df.columns[1:]        # TODO: 국적 제외하고 항공사만 가져오시오.
    항공사별_합계 = df[항공사목록].sum()  # TODO: 각 항공사별 전체 합계를 구하시오.

    plt.bar(항공사별_합계.index, 항공사별_합계.values)                    # TODO: x축 항공사명, y축 합계로 막대그래프를 그리시오.
    plt.title("항공사별 외국인 조종사수")                        # TODO: 적절한 제목을 작성하시오.
    plt.xlabel("항공사")
    plt.ylabel("조종사 수")
    plt.xticks(rotation=45)             # TODO: X축 글자가 겹치지 않게 기울이시오.
    plt.tight_layout()
    plt.show()
# 막대그래프()

def 파이차트():
    # 대한항공 조종사가 1명 이상인 국적만 필터링
    df_대한항공 = df[df['대한항공'] >= 1]

    plt.pie(
        df_대한항공['대한항공'], labels=df_대한항공['국적'], autopct="%1.1f%%")
    plt.title("대한항공 외국인 조종사 국적 비율")
    plt.show()
# 파이차트()

def 가로막대그래프():
    # 각 국적별로 전체 항공사 합계 구하기
    df['전체합계'] = df[df.columns[1:]].sum(axis=1)

    # 전체합계가 0보다 큰 국적만 필터링
    df_합계 = df[df['전체합계'] > 0]

    plt.barh(df_합계['국적'], df_합계['전체합계'])
    plt.title("국적별 전체 외국인 조종사 수")
    plt.xlabel("국가")
    plt.tight_layout()
    plt.show()
# 가로막대그래프()

def 히스토그램():
    plt.hist(df['대한항공'], bins=10)   # TODO: 대한항공 컬럼, 구간 10개
    plt.title("대한항공 국적별 조종사수 분포")
    plt.xlabel("조종사 수")
    plt.ylabel("국적 수")
    plt.show()
# 히스토그램()

def 그래프이미지로저장():
    항공사별_합계 = df[df.columns[1:]].sum()

    plt.bar(항공사별_합계.index, 항공사별_합계.values)
    plt.title("항공사별 외국인 조종사 수")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("외국인조종사_차트.png")
    plt.show()
그래프이미지로저장()