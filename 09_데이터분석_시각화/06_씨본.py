'''
Seaborn python 데이터 시각화 라이브러리
matplotlib 기반으로 만들어졌지만 훨씬 적은 코드로 예쁜 그래프 그릴수 있다.
판다스 DataFrame과 함께 데이터 분석할때 자주 사용

주 종류
scatterplot 산점도 분포 파악
lineplot    선 그래프 추세 파악
histplot    히스토그램
barplot     바 그래프 카테고리별 평균
boxplot     분포 이상치 확인
heatmap     색상으로 상관관계

설치 방법
pip install seaborn


'''
import os

import seaborn as sns
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


df = sns.load_dataset("tips")

def 판다스를_이용하여_데이터구조확인():
    print(df.head())
    print("=="*80)
    print(df.shape)
    print("=="*80)
    print(df.columns)
    print("=="*80)
    print(df.dtypes)
    print("=="*80)
    print(df.describe())
# 판다스를_이용하여_데이터구조확인()
def 맷플롯립을_이용하여_데이터눈으로확인():
    sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
    plt.title("계산서 vs 팁")
    plt.show()

def seaborn에서_만든데이터_나의컴퓨터에_판다스로csv_저장하기():
    df.to_csv("seaborn_tips.csv",index=False,encoding="utf-8-sig")
    print("seaborn에서 만든 데이터 csv로 저장 완료")
# seaborn에서_만든데이터_나의컴퓨터에_판다스로csv_저장하기()

def seaborn_dataset_all_save():
    저장할폴더 = "seaborn_data"
    os.makedirs(저장할폴더,exist_ok=True)
    dataset = ['tips','titanic','iris','penguins','flights','diamonds','mpg']
    for name in dataset:
        df = sns.load_dataset(name)
        df.to_csv(f"{저장할폴더}/seaborn_{name}.csv",index=False,encoding="utf-8-sig")
        print(f"seaborn_{name}.csv 저장완료")

seaborn_dataset_all_save()