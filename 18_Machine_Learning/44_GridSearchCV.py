from sklearn.svm import SVC, SVR
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler

"""
GridSearchCV
는 SVM 전용이 아니라 sklearn 모델이면 다 가능~
대신 모델마다 파라미터가 다르기 때문에
    그리드파람 = {
        'C' : [0.1,1,10,100],           # 4가지 조합
        'gamma' : [0.001,0.01,0.1,1],   # 4가지 조합
        'kernel' : ['rbf','linear']         # 2가지 조합
    }
은 모델에 따라 키이름과 속성데이터를 변경해야 할 수 있다.
그리드파람_랜덤포레스트 -> n_estimators, max_depth , ...
그리드파람_KNN          -> n_neighbors
그리드파람_SVC          -> C, gamma, kernel, ...
"""

def 최적파라미터자동탐색_gridSearchCV():
    # 어떤 C, gamma 값이 최선인지 자동으로 다 시도하는 방법
    # 자동에 대한 설정값은 개발자가 직접 해주어야한다.

    X,y = load_iris(return_X_y=True)
    X_trian, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    스케일러 = StandardScaler()
    # 위에서 분리한 80 20 데이터를 스케일러로 정돈한 후 다시 X_train 과 X_test에 담아준다.
    X_trian = 스케일러.fit_transform(X_trian)
    X_test = 스케일러.transform(X_test)

    그리드파람 = {
        'C' : [0.1,1,10,100],           # 4가지 조합
        'gamma' : [0.001,0.01,0.1,1],   # 4가지 조합
        'kernel' : ['rbf','linear']         # 2가지 조합
    }
    # 4 x 4 x 2 = 32 가지 조합
    # cv = 5 교차 검증을 통해
    # 총 32 x5 = 160 번 학습

    모델 = GridSearchCV(
        SVC(),
        그리드파람,
        cv=5,       # 몇 등분해서 검증할 것인가 cv=5 전체데이터를 5등분으로 나눠서 검증
        scoring='accuracy',
        n_jobs=-1,
        verbose=1 # 진행상황을 얼마나 자세히 출력해서 보여줄까?
        # 0 아무것도 안보여줄거다
    )
최적파라미터자동탐색_gridSearchCV()