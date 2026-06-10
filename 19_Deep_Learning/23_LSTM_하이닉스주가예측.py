# TODO___ 아래 라이브러리를 import 하세요
# 힌트: pandas, numpy, matplotlib.pyplot
# 힌트: sklearn.preprocessing 에서 MinMaxScaler
# 힌트: tensorflow.keras.models 에서 Sequential
# 힌트: tensorflow.keras.layers 에서 Input, LSTM, Dense

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

# TODO___ CSV 를 불러와서 종가(Close)만 반환하세요
# 힌트: pd.read_csv(경로, index_col=0, skiprows=[1, 2])
# 힌트: df.index = pd.to_datetime(df.index)
# 힌트: df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
# 힌트: return df[['Close']]

df = pd.read_csv('SK하이닉스.csv', index_col=0, skiprows=[1,2])
df.index = pd.to_datetime(df.index)
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
close = df[['Close']]
print(close.tail())

# TODO___ 종가를 0~1 사이로 정규화 하세요
# 힌트: MinMaxScaler() 로 변환기 생성
# 힌트: scaler.fit_transform(close) 로 변환
# 힌트: 나중에 역정규화할 때 필요하니까 scaler 도 저장해두기

scaler = MinMaxScaler()
scaled = scaler.fit_transform(close)

# TODO___ 60일치 데이터로 다음날을 예측하는 시퀀스를 만드세요
# 힌트: X 에는 data[i-window:i] (60일치 입력)
# 힌트: y 에는 data[i]           (다음날 정답)
# 힌트: 마지막에 np.array() 로 변환

X, y = [], []
for i in range(120 , len(scaled)):
    X.append(scaled[i-120:i])
    y.append(scaled[i])
X, y = np.array(X), np.array(y)
print(X.shape)  # (날짜수, 60, 1)

# TODO___ 전체 데이터를 80% 학습용, 20% 테스트용으로 나누세요
# 힌트: split = int(len(X) * 0.8)
# 힌트: X[:split] 이 학습용, X[split:] 이 테스트용

split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# TODO___ LSTM 모델을 만드세요
# 힌트: Input shape = (60, 1)
# 힌트: LSTM(64, return_sequences=True) → LSTM(32) → Dense(1) 순서
# 힌트: compile optimizer='adam', loss='mse'

model = Sequential([
    Input(shape=(120,1)),
    LSTM(128, return_sequences=True),
    LSTM(32),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.summary()

# TODO___ 모델을 학습시키세요
# 힌트: epochs=20, batch_size=32, validation_split=0.1

model.fit(X_train, y_train,
          epochs=20,
          batch_size=32,
          validation_split=0.1)

# TODO___ 예측하고 실제 주가로 되돌리세요
# 힌트: model.predict(X_test) 로 예측 (결과는 아직 0~1)
# 힌트: scaler.inverse_transform() 으로 실제 주가로 복원

pred = model.predict(X_test)
pred_price = scaler.inverse_transform(pred)
real_price = scaler.inverse_transform(y_test)

# TODO___ 실제 주가와 예측 주가를 그래프로 그리세요
# 힌트: plt.figure(figsize=(12, 5))
# 힌트: plt.plot() 두 번 — 실제주가, 예측주가
# 힌트: plt.legend() 로 범례 표시

plt.figure(figsize=(12,5))
plt.plot(real_price, label='실제 주가')
plt.plot(pred_price, label='예측 주가')
plt.title('SK하이닉스 주가 예측 (LSTM)')
plt.legend()
plt.show()
