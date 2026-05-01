import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("소상공인시장진흥공단_전국 카페 점포수_11_04_2019.csv", encoding="cp949")
업소수 = np.array(df["업소수"])

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def 데이터확인():

    print(df.head())
    print(df.shape)
    print(업소수)
데이터확인()

def 통계분석():
    print(np.sum(업소수))
    print(np.max(업소수))
    print(np.min(업소수))
    print(np.mean(업소수))
    print(np.std(업소수)) #표준편차 수치가 크면 데이터의 분산이 많이 된다는 것을 의미
    print(np.median(업소수))
    # 1. 전체 기간 중 총 업소수 합계를 출력하세요
    # 2. 가장 많은 카페가 있던 달의 업소수를 출력하세요
    # 3. 가장 적은 카페가 있던 달의 업소수를 출력하세요
    # 4. 월평균 카페 점포수를 출력하세요
    # 5. 표준편차를 출력하고, 수치가 크면 어떤 의미인지 주석으로 작성하세요
    # 6. 중앙값을 출력하세요
# 통계분석()

def 인덱싱_슬라이싱_필터링():
    print(업소수[0])
    print(업소수[-1])
    print(업소수[5:16])
    print(업소수[업소수 >= 80000])
    print(업소수[업소수 > np.mean(업소수)])
# 인덱싱_슬라이싱_필터링()

def 배열연산응용():
    만단위 = 업소수 / 10000
    print(만단위)
    전월대비증감 = 업소수[1:] - 업소수[:-1]
    print(전월대비증감)


def 시각화():
    plt.figure(figsize=(12,5))
    plt.plot(df['기준월'],df['업소수'],marker='o')
    plt.title("전국 카페 월별 점포수 변화")
    plt.xlabel("기준월")
    plt.ylabel("업소수")
    plt.xticks(rotation=45)
    plt.show()
