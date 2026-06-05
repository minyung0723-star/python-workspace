"""
CNN = Convolutional Neural Network(합성곱 신경망)
사람의 눈이 사진을 보는 방식을 컴퓨터로 흉내낸 것

사람이 고양이 사진을 볼 때 → 귀, 수염, 눈을 보고 고양이다! 라고 알아채는 것처럼

Conv2D = 특징을 찾는 돋보기
- 이미지에서 특징(feature) 을 찾는 필터
마치 돋보기로 사진을 훑는 것처럼, 작은 창문(필터)이 이미지 위를 쭉 지나가면서 특징 찾기
사진을 보고 사진 특징을 컬럼으로 정리하겠다.
필터가 찾은 것들 :
    첫 번째 레이어 : 선,점, 경계선 같은 단순한 것들

"""
import tensorflow as tf
from pygame.midi import Input
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# 사진을 확인하고 분류하는 로봇 뇌 만들기
#        뇌 만들기 시작
로봇뇌 = Sequential([
    # 가장 먼저 사물을 보는 로봇 눈 만들기 로봇의 눈은 사진이 흑백인지 사진 사이즈는 어떻게 되는지 생성
    Input((32, 32, 3)),
    # Input((32, 32, 1)), 흑백 사진의 경우 초록 파랑 빨강이 필요 없으므로 1로 작성
    Conv2D(32,(3,3),activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')


    # 레거시 방법
])

# 로봇뇌 학습 준비

로봇뇌.compile(
    optimizer='adam',

    loss='sparse_categorical_crossentrophy', # 틀린 정도 측정 3개 이상은 옆에 있는 loss 많이 사용
    metrics=['accuracy'] # 정확도 측정
)

# 로봇뇌의 구조를 보는 메서드
로봇뇌.summary()
















