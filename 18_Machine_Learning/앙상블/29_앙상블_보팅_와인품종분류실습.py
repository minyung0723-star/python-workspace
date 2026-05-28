"""
앙상블 실습 - 와인 품종 분류
- 와인의 알콜, 산도, 색상 등 13개 성분으로 와인 품종 3가지 분류
- 아이리스(=붓꽃) 보다 KNN이 약해서 보팅(모델 투표를 통한 결과) 효과가 더 잘 보임

예)
    와인 데이터를 X에 넣으면 품종을 예측
    X = [[알콜, 산도, 색상강도, 플라보노이드, ...]]

    lr.predict(X)  # 로지스틱 회귀가 판단
    dt.predict(X)  # 결  정  트 리가 판단
    knn.predict(X) # K    N    N 이 판단
"""

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

로지스틱모델 = LogisticRegression(max_iter=20000) # LogisticRegression 확률에 따른 분류 진행
결정트리모델 = DecisionTreeClassifier()
KNN모델 = KNeighborsClassifier()

def 하드투표기능():
    하드투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting='hard'
    )
    하드투표.fit(X_train,y_train)
    결과 = 하드투표.predict(X_test)
    print(f"하드 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")
def 소프트투표기능():
    소프트투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting='soft'
    )
    소프트투표.fit(X_train,y_train)
    결과 = 소프트투표.predict(X_test)
    print(f"소프트 보팅 정확도 : {accuracy_score(y_test, 결과):.4f}")

def 하드_소프트투표기능():

    개별모델들 = [('로지스틱 회귀', 로지스틱모델), ('결정 트리', 결정트리모델), ('KNN', KNN모델)]

    하드투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting='hard'
    )

    소프트투표 = VotingClassifier(
        estimators=[
            ('lr',로지스틱모델),
            ('dt',결정트리모델),
            ('knn',KNN모델)
        ],
        voting='soft'
    )

    for 이름, 모델 in [('하드투표', 하드투표), ('소프트투표', 소프트투표)]:
        모델.fit(X_train, y_train)
        결과 = 모델.predict(X_test)
        print(f"{이름} 정확도 : {accuracy_score(y_test, 결과):.4f}")

    for 이름, 모델 in 개별모델들:
        모델.fit(X_train, y_train)
        예측 = 모델.predict(X_test)
        정확도 = accuracy_score(y_test, 예측)
        print(f"{이름} 정확도 : {정확도:.4f}")

하드_소프트투표기능()

