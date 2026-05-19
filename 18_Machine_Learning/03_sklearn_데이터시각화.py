import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# 수집한 데이터 시각화하여 확인

# 1. 산점도를 이용해서 꽃들이 어디 모여있는지 조회
붓꽃 = load_iris()
X = 붓꽃.data
y = 붓꽃.target

# 종류별로 다른 색을 지정하여 조회
색깔 = ['red','blue','green']
종류 = ['setosa','versicolor','virginica']

plt.figure(figsize=(8,5)) # 그래프가 들어있는 화면 전체 크기 설정
for i in range(3): # setosa versicolor virginica 정답이 3개이므로 012 까지 조회 3은 자동으로 하지 않는 방식
    plt.scatter( # 산점도 분포를 할 때
        X[y == i, 0], # x축 : 꽃받침 길이
        y[y == i, 0], # y축 : 꽃받침 너비
        color=색깔[i],
        lable=종류[i]
    )

plt.xlabel("꽃받침 길이")
plt.ylabel("꽃받침 너비")
plt.title("붓꽃 종류별 분포")
plt.legend() # 어떤색이 어떤 종류인지 표기 화면에 보여주기
plt.show() # 위에 작성한 것을 토대로 개발자의 눈에서 확인하기
