import numpy as np

def 기본_배열_생성():
    영_7 = np.zeros(7)
    일_4 = np.ones(4)
    건너뛰기 = np.arange(0, 20, 3)
    균등간격 = np.linspace(0, 1, 6)
    print(영_7)
    print(일_4)
    print(건너뛰기)
    print(균등간격)

def 파이썬_리스트_vs_NumPy_연산():
    a = np.array([10, 20, 30])
    b = np.array([1, 2, 3])
    c = [10,20,30]
    d = [1,2,3]

    더하기 = a + b
    빼기 = a - b
    곱하기 = a * b
    나누기 = a / b
    파이썬더하기 = c + d


    print("넘파이 더하기 : ", 더하기)
    print("넘파이 빼기 : ", 빼기)
    print("넘파이 곱하기 : ", 곱하기)
    print("넘파이 나누기 : ", 나누기)
    print("파이썬 더하기 : ", 파이썬더하기)
    # 파이썬 더하기는 파이썬 더하기 :  [10, 20, 30, 1, 2, 3] 형태로 문자들이 합해지고
    # 넘파이 더하기는 계산을해서 넘파이 더하기 :  [11 22 33] 형태로 출력한다


def 인덱싱과_슬라이싱():
    a = np.array([5, 15, 25, 35, 45, 55])
    print("첫 번째 값 : ", a[0])
    print("마지막 값 : ",a[-1])
    print("2번 부터 4번까지 슬라이싱 : ",a[2:4])
    print("30보다 큰 값 : ", a[a > 30])
    print("15로 나누어 떨어지는 값 : ", a[a % 15 == 0])


def 통계_함수_활용():
    scores = np.array([88, 72, 95, 60, 83, 77, 91, 68])

    총합 = np.sum(scores)
    높은점수 = np.max(scores)
    낮은점수 = np.min(scores)
    평균 = np.mean(scores)
    표준편차 = np.std(scores)
    중앙값 = np.median(scores)

    print(총합)
    print(높은점수)
    print(낮은점수)
    print(평균)
    print(표준편차)
    print(중앙값)


def 종합_문제():
    # 아래 배열은 어느 가게의 7일간 일별 매출액(만원)입니다.
    sales = np.array([120, 85, 200, 150, 95, 175, 210])

    총매출 = np.sum(sales)
    평균매출 = np.mean(sales)
    높은매출 = np.max(sales)
    낮은매출 = np.min(sales)
    부가세포함값 = sales * 1.1

    print("7일 총 매출 : ", 총매출)
    print("하루 평균 매출 : ", 평균매출)
    print(f"가장 높은 매출 : {높은매출}, 가장 낮은 매출 : {낮은매출}")
    print("평균보다 높은 매출이 발생한날 : ", sales[sales > 평균매출])
    print("부가세 포함 매출 : ", 부가세포함값)


