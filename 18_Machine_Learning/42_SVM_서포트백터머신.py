"""
SVM
- 데이터를 가장 잘 나누는 선(경계)를 찾는 알고리즘
- 마진(Margin) : 경계선에서 각 클래스의 가장 가까운 점의 거리 X 2
- 커널 트릭(kernel) : 데이터를
    - 데이터가 적어도 잘 작동함

- SVM 스케일링 필수
  스케일링 : 숫자 데이터 범위를 스케일링이 확인해서 0~1 사이의 범위로 나열

  데이터가 너무 엉망으로 섞여 있어 선을
"""
# 데이터가 있는데 데이터 컬럼마다 숫자가 천차만별
# 나이컬럼 연봉컬럼 자녀수컬럼 부서인원컬럼
# 0~100     천~억     0~10        0~100 ..
# 스케일링을 사용해서 각각 컬럼을 -3~3 0~1 와 같이 알아서 스케일링으로
# 범위를 비슷하게 만들어서 계산 처리를 할 수 있게 세팅해주는 것이
# 스 케 일 링!
from sklearn.svm import SVC # Support Vector Classifier
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# make_classification =  가짜 데이터를 만들어서 임의적으로 무언가 확인할 때 사용
# 현재 데이터는 중요하지 않고 딱히 생각나는 데이터는 없지만

def 마진확인방법():
    X,y = make_classification(
        n_samples=100,  # 데이터 샘플 개수
        n_features=2,   # 데이터 컬럼 개수
        n_redundant=0,  # 중복 컬럼 개수
        random_state=42 #랜덤 시드 고정
    )
    # C 파라미터 = 마진관련
    # C 작을수록   마진 넓게 일   반  화↑ 오분류 허용
    # C 높을수록   마진 좁게 훈련 정확도↑ 과적합 위험
    model_wide = SVC(C=0.1, kernel='linear')
    model_tight = SVC(C=100, kernel='linear')

    model_wide.fit(X,y)
    model_tight.fit(X,y)
    print(f"넓은 마진 서포트 벡터 수 : {len(model_wide.support_vectors_)}")
    print(f"좁은 마진 서포트 벡터 수 : {len(model_tight.support_vectors_)}")





















