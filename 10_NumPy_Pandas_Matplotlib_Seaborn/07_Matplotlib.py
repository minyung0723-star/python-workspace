'''
Matplotlib
- 파이썬의 가장 기본적인 시각화 라이브러리
그래프의 모든 것을 직접 제어할 수 있다.

'''
# matplotlib 라이브러리에서 특정 기능 pyplot 을 가지고와서 그래프를 그릴 것인데
# 명칭이 너무 길기 때문에 plt 별칭으로 축소해서 부를 것이다.
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
x = [1,2,3,4,5]
y = [2,4,1,5,3]

# 기본 선형 그래프
plt.plot(x,y)
plt.title("기본 선 그래프")
plt.xlabel("x축")
plt.ylabel("y축")
plt.show()

# 막대 그래프 = 값 비교
plt.bar(['A','B','C'], [10,20,15])
plt.show() #그래프를 그릴 때마다 show() 를 하지 않으면 모든 그래프가 누적된채로 보여지게된다.
# 보여진 그래프는 x창을 누르는순간 메모리에서 사라지게된다.

# 산점도 = 두 변수의 관계
plt.scatter(x, y)
plt.show()

# 히스토그램
data = np.random.randn(1000)
plt.hist(data, bins=30)