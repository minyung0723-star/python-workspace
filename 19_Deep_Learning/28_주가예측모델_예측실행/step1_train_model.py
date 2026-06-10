"""
==================
STEP 1 : 모델 학습 & 저장

이 파일에서 하는 일 :
1. 삼성전자 5분봉 데이터를 야후 피아낸스 기능 다운로드
2. 데이터를 MinMax 스케일러를 이용해서 0~1 사이로 정규화
3. LSTM 신경망 모델 학습
4. 학습된 모델과 스케일러를 모델파일 keras 로 저장

과거 몇 개 봉을 들고 다음을 예측할 것인지
전체 데이터를 몇 번 반복할 것인지
한 번에 몇 개 씩 묶어서 학습할 지

몇 분 봉을 기준으로 할 것인지는 스스로 선택

"""
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input

WINDOW = 10

삼성주식 = yf.download("005930.KS", period='60d', interval="5m")
삼성주식.to_csv('samsung.csv')

종가 = 삼성주식['Close'].dropna().values.reshape(-1, 1)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(종가)

X, y = [], []
for i in range(WINDOW, len(scaled)):
    X.append(scaled[i-WINDOW:i])
    y.append(scaled[i])
X, y = np.array(X), np.array(y)


model = Sequential([
    Input(shape=(WINDOW, 1)),
    LSTM(64, return_sequences=True),
    LSTM(32),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.summary()

model.fit(
    X, y,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

