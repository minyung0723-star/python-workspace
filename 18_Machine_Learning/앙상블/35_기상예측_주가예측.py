"""
날씨 데이터로 내일 비 올지 예측
기온 / 습도 / 풍속 → 비 올지 안 올지 분류
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def 날씨예측():

    # TODO 1: CSV 파일 읽기
    df = pd.read_csv("../csvs/weather_forecast_data.csv", encoding="utf-8")

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print("\n=== 몇 행 몇 열? ===")
    print(df.shape)

    # TODO 2: 결측치(빈값) 채우기
    df['Temperature']  = df['Temperature'].fillna(df['Temperature'].mean())
    df['Humidity']     = df['Humidity'].fillna(df['Humidity'].mean())
    df['Wind_Speed']   = df['Wind_Speed'].fillna(df['Wind_Speed'].mean())
    df['Precipitation']= df['Precipitation'].fillna(df['Precipitation'].mean())

    # TODO 3: 사용할 피처(컬럼) 리스트 직접 채우기
    features = ['Temperature', 'Humidity', 'Wind_Speed', 'Precipitation']

    # TODO 4: X (입력), y (정답) 나누기
    X = df[features]
    y = df['Rain']

    # TODO 5: 훈련/테스트 데이터 나누기
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TODO 6: 랜덤포레스트 모델 만들기
    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)

    # TODO 7: 모델 학습시키기
    rf.fit(X_train, y_train)

    # TODO 8: 테스트 데이터로 예측하기
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['맑음', '비']))

    # =======================================
    # VotingClassifier (3개 모델이 투표)
    # =======================================

    # TODO 9: 3개 모델 각각 만들기
    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    # TODO 10: VotingClassifier 만들기
    voting = VotingClassifier(
        estimators=[('rf', model1), ('dt', model2), ('lr', model3)],
        voting='hard'
    )

    # TODO 11: voting 모델 학습시키기
    voting.fit(X_train, y_train)

    # TODO 12: voting 모델로 예측하기
    pred_voting = voting.predict(X_test)

    print("\n=== 보팅 결과 (3개 모델 투표) ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['맑음', '비']))

    # TODO 13: 랜덤포레스트 vs 보팅 정확도 비교 출력
    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 정확도 : {accuracy_score(y_test, pred_rf): .4f}")
    print(f"보팅        정확도 : {accuracy_score(y_test, pred_voting): .4f}")
    if accuracy_score(y_test, pred_voting) > accuracy_score(y_test, pred_rf):
        print("보팅이 더 좋다.")
    else:
        print("랜덤포레스트가 더 좋다.")

    # TODO 14: 피처 중요도 출력
    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)

    print("\n=== 비 오는 데 영향주는 요소 순위 ===")
    print(중요도)


def 주식예측():

    # TODO 1: CSV 파일 읽기
    df = pd.read_csv("csvs/stock_price_data.csv", encoding="utf-8") # 파일명은 환경에 맞게 수정 가능

    print("=== 데이터 미리보기 ===")
    print(df.head())
    print("\n=== 컬럼 목록 ===")
    print(df.columns.tolist())
    print("\n=== 결측치 확인 ===")
    print(df.isnull().sum())
    print("\n=== 몇 행 몇 열? ===")
    print(df.shape)

    # TODO 2: 정답 컬럼 Target 만들기
    df['Target'] = (df['Close'] > df['Open']).astype(int)

    print(f"\n상승일 수 : {df['Target'].sum()}일")
    print(f"하락일 수 : {(df['Target'] == 0).sum()}일")

    # TODO 3: 결측치(빈값) 채우기
    df['Open']   = df['Open'].fillna(df['Open'].mean())
    df['High']   = df['High'].fillna(df['High'].mean())
    df['Low']    = df['Low'].fillna(df['Low'].mean())
    df['Volume'] = df['Volume'].fillna(df['Volume'].mean())

    # TODO 4: 사용할 피처(컬럼) 리스트 채우기
    features = ['Open', 'High', 'Low', 'Volume']

    # TODO 5: X (입력), y (정답) 나누기
    X = df[features]
    y = df['Target']

    # TODO 6: 훈련/테스트 데이터 나누기
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # TODO 7: 랜덤포레스트 모델 만들기
    rf = RandomForestClassifier(n_estimators=100, max_features='sqrt', random_state=42)

    # TODO 8: 모델 학습시키기
    rf.fit(X_train, y_train)

    # TODO 9: 테스트 데이터로 예측하기
    pred_rf = rf.predict(X_test)

    print("\n=== 랜덤 포레스트 결과 ===")
    print(f"정확도 : {accuracy_score(y_test, pred_rf):.4f}")
    print(classification_report(y_test, pred_rf, target_names=['하락', '상승']))

    # =======================================
    # VotingClassifier (3개 모델이 투표!)
    # =======================================

    # TODO 10: 3개 모델 각각 만들기
    model1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model2 = DecisionTreeClassifier(random_state=42)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    # TODO 11: VotingClassifier 만들기
    voting = VotingClassifier(
        estimators=[('rf', model1), ('dt', model2), ('lr', model3)],
        voting='hard'
    )

    # TODO 12: voting 모델 학습시키기
    voting.fit(X_train, y_train)

    # TODO 13: voting 모델로 예측하기
    pred_voting = voting.predict(X_test)

    print("\n=== 보팅 결과 (3개 모델 투표) ===")
    print(f"정확도 : {accuracy_score(y_test, pred_voting):.4f}")
    print(classification_report(y_test, pred_voting, target_names=['하락', '상승']))

    # TODO 14: 랜덤포레스트 vs 보팅 정확도 비교 출력
    print("\n=== 모델 비교 ===")
    print(f"랜덤포레스트 정확도 : {accuracy_score(y_test, pred_rf): .4f}")
    print(f"보팅        정확도 : {accuracy_score(y_test, pred_voting): .4f}")
    if accuracy_score(y_test, pred_voting) > accuracy_score(y_test, pred_rf):
        print("보팅이 더 좋다.")
    else:
        print("랜덤포레스트가 더 좋다.")

    # TODO 15: 피처 중요도 출력
    중요도 = pd.DataFrame({
        '특성': features,
        '중요도': rf.feature_importances_
    }).sort_values('중요도', ascending=False)

    print("\n=== 주가 예측에 영향주는 요소 순위 ===")
    print(중요도)


# 함수 실행
날씨예측()
print("\n" + "="*40 + "\n")
주식예측()