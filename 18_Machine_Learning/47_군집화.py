"""
군집화
- 라벨(정답)이 없는 데이터를 비슷한 것끼리 자동으로 그룹 묶기
차원 축소 = 컬럼(열)을 줄이는 것
군   집화 = 행(데이터)을 그룹으로 묶는 것

쇼핑몰 고객 1만명
    → 아무 정보 없이 구매패턴만 보고

    그룹 A : 자주사고 많이씀(VIP)
    그룹 B : 가끔사고 적게씀(일반)
    그룹 C : 오래전에 사고 안옴(이탈위험)

    → 정답이 없으나 AI가 알아서 스스로 그룹 나눔

간단히 비교하자

            차원축소               군집화               분류             회귀
목적       컬럼 줄이기            그룹 묶기          정답 맞추기        숫자 예측
라벨         불필요                불필요               필요              필요
결과      압축된 데이터           그룹 번호             예측값         연속된 숫자
예시     100컬럼 → 2컬럼       고객등급 자동분류      스팸메일판별       주가 예측
-------------------------------------------------------------------------------------
모델       PCA, 커널PCA        K-Means, DBSCAN       SVM, KNN          선형회귀
           LDA, LLE, NMF        계층적 군집화        로지스틱회귀      릿지 , 라쏘
                                                    랜덤포레스트        XGBoost
지도 학습 - 정답이 있는 상태에서 정답 따라 모델 학습
비지도 학습 - 정답이 없는 상태에서 진행하는 모델 학습
예를 들어           그룹에 정답이 있나?         그냥 데이터를 보고 구분하는 것으로 정답이 없다

군집화 3가지
1. K-Means
- 내가 그룹 수를 직접 정함 / 중심점을 기준으로 가까운 것끼리 묶음
- 빠르고 간단 / 가장 많이 사용
- 그룹수를 미리 알아야 하며, 원형 데이터에만 잘 된다.
- 예 : 고객을 3등급으로 나눠줘

2. DBSCAN
- 밀집된 곳 = 그룹
- 혼자 동떨어진 데이터 = 노이즈(이상치)로 처리
- 그룹 수 안 정해도 됨
- 이상한 데이터는 자동 제거


3. 계층적 군집화
- 가장 비슷한 것끼리 합쳐가며 트리(덴드로그램)구조로 시각화
- 그룹 수 안 정해도 됨
- 트리로 과정을 눈으로 확인 가능
- 데이터가 많으면 매우 느림
- 예 : 생물 분류, 언어 계통도

K-Means
DBSCAN
계층적

코드 또한 그룹으로 묶거나 분석하는 형태를 주로 띈다.
모델결과를 주로 시각화해서 표기
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import alpha
from sklearn.datasets import make_blobs,make_moons
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1,3,figsize=(15,4))
fig.suptitle('군집화 3가지 비교')

X,y = make_blobs(n_samples=300, centers=3, random_state=42)
# make_blobs 동글동글한 덩어리 데이터 생성
# n_samples = 300 데이터 300개
# centers = 3 덩어리 3개

# ==========================================================
# 1. K-Means
# ==========================================================
kmeans = KMeans(n_clusters=3, random_state=42)
labels_km = kmeans.fit_predict(X)
# fit_predict = 학습하고 바로 그룹번호 반환
ax = axes[0]
ax.scatter(X[:,0],X[:,1],c=labels_km,cmap='Set1',alpha=0.7)
ax.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    c='black',marker='X',s=200, label='중심점'
           )
ax.set_title('K-Means')
ax.legend()

# ==========================================================
# 2. DBSCAN
# 꼬인 데이터에 강함
# make_moon 초승달 모양 2개 데이터 K-Means 으로 나눌 수 없는 없데이터
# ==========================================================
X_moon, _ = make_moons(n_samples=300, noise=0.1, random_state=42)
dbscan = DBSCAN(eps=0.2, min_samples=5)
# 거리와 그룹별 인원 수는 개발자가 지정
labels_db = dbscan.fit_predict(X_moon) # 초승달 데이터에 위 규칙 적용해서 그룹 번호 붙여줘

ax = axes[1]
ax.scatter(X_moon[:,0],X_moon[:,1],c=labels_db,cmap='Set1',alpha=0.7)
ax.set_title('DBSCAN 노이즈(-1로 표기)')

# ==========================================================
# 3. 계층적 군집화
# ==========================================================

hc = AgglomerativeClustering(n_clusters=3)

# 그룹 개수는 개발자 분석가가 지정
labels_hc = hc.fit_predict(X)

ax = axes[2]
ax.scatter(X[:,0],X[:,1],c=labels_hc,cmap='Set1',alpha=0.7)
ax.set_title('계층적 군집화')

plt.tight_layout()
plt.show()







