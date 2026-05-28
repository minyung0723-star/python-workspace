"""
실습 과제 : 스팸 문자 분류기 - 모델 학습
데이터    : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
저장위치  : csvs/spam.csv
"""

import pandas as pd
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ================================
# STEP 1. 데이터 불러오기
# ================================
df = pd.read_csv(
    'csvs/spam.csv',
    encoding='latin-1',
    usecols=[0, 1]
)

# TODO 1: 컬럼 이름을 'label', 'message' 로 바꾸기
df.columns = ___

# TODO 2: 상위 5개 출력
print(___)

# TODO 3: label 값 개수 출력
print(___)


# ================================
# STEP 2. 데이터 분리
# ================================

# TODO 4: X 에 message, y 에 label 담기
X = df[___]
y = df[___]

# TODO 5: train_test_split 8:2, random_state=42
X_train, X_test, y_train, y_test = train_test_split(___, ___, test_size=___, random_state=___)


# ================================
# STEP 3. 텍스트 → 숫자 변환
# ================================

# TODO 6: CountVectorizer 생성
vectorizer = ___()

# TODO 7: X_train 은 fit_transform / X_test 는 transform
X_train_vec = vectorizer.___(X_train)
X_test_vec  = vectorizer.___(X_test)


# ================================
# STEP 4. 모델 학습
# ================================

# TODO 8: MultinomialNB 생성 후 학습
model = ___()
model.fit(___, ___)


# ================================
# STEP 5. 정확도 확인
# ================================

# TODO 9: accuracy_score 로 정확도 계산 후 출력 (소수점 1자리 %)
acc = accuracy_score(___, model.predict(___))
print(f"정확도: {acc * 100:.1f}%")


# ================================
# STEP 6. 모델 저장
# digit 프로젝트와 다른점 :
# 텍스트 모델은 vectorizer 도 같이 저장해야 한다
# 글자→숫자 변환기도 app.py 에서 그대로 써야 하기 때문
# ================================

# TODO 10: model 과 vectorizer 를 딕셔너리로 묶어서 pkl 저장
파일명 = f'spam_model_{acc * 100:.1f}.pkl'
with open(파일명, '___') as f:
    pickle.dump(___, f)

print(f"저장완료: {파일명}")