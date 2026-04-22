# 1번 문제
def problem1():
    과일들 = ["사과","바나나","포도"]
    print(f"과일개수: {len(과일들)}")
# problem1()

# 2번 문제
def multiply(a,b):
    결과 = a * b
    print(f"{a}곱하기 {b}는 {결과} 입니다")
# multiply(6,7)

# 3번 문제
def welcome(name):
    print(f"{name}님, 환영합니다!")
# welcome("철수")

# 4번 문제
def average(a, b, c):
    평균 = (a + b + c) / 3
    print(f"{a}, {b}, {c}의 평균은 {평균}입니다.")
# average(10,20,30)

# 5번 문제
def say_hi(name, greeting="좋은 하루에요"):
    print(f"{greeting}, {name}님!")

# say_hi("지수")
# say_hi("민준", "오랜만이에요")

# 6번 문제
def order(menu, size, temperature):
    print(f"{temperature} {size} {menu} 주문 완료!")
# order("아메리카노","라지","아이스")

# 7번 문제
def is_even(n):
    결과 = n % 2 == 0
    print(f"{n}은 짝수입니다 :{결과}")
# is_even(7)

# 8번 문제
def introduce(name, age=20, city="서울"):
    print(f"{name} / {age}세 / {city}")
# introduce("철수")

# 9번 문제
def profile(name, age):
    print(f"이름: {name} / 나이: {age}세")
# profile(age=23,name="하은")

# 10번 문제
def add(a,b):
    return a+b
def show(n):
    print(f"결과는 {n}입니다.")
# show(add(7,8))