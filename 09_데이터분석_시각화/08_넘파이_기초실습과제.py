import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("소상공인시장진흥공단_전국 카페 점포수_11_04_2019.csv", encoding="cp949")
업소수 = np.array(df["업소수"])

def 배열만들기():
    print(np.zeros(6))
    print(np.ones(5))
    print(np.arange(0,30,5))
    print(np.linspace(0,1,8))
# 배열만들기()

def 배열연산():
    a = np.array([10, 30, 50])
    b = np.array([2, 3, 5])
    c = [10, 30, 50]
    d = [2, 3, 5]
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(c + d)
    # 파이썬 리스트는 리스트 를 합쳐서 나열하고 넘파이 결과는 리스트 안에 숫자들이 계산되어 출력된다
# 배열연산()

def 인덱싱_슬라이싱_필터링():
    a = np.array([10, 20, 30, 40, 50, 60, 70])
    print(a[0])
    print(a[-1])
    print(a[2:6])
    print(a[a > 40])
    print(a[a % 20 == 0])
# 인덱싱_슬라이싱_필터링()

def 통계함수():
    scores = np.array([70, 85, 90, 55, 78, 92, 63, 88])
    print(np.sum(scores))
    print(np.max(scores))
    print(np.min(scores))
    print(np.mean(scores))
    print(np.std(scores))
    print(np.median(scores))
# 통계함수()
