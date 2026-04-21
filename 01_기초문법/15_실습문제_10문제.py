def 문제1():
    name = "홍길동"
    age = 25
    print(f"안녕하세요! 저는 {name}이고 {age}살입니다")
    # 아래처럼 출력되도록 완성하세요
    # 안녕하세요! 저는 홍길동이고 25살입니다.

# 문제1()

def 문제2():
    name= input("이름을 입력하세요 : ")
    age= int(input("나이를 입력하세요 : "))
    print(f"{name}님은 내년에 {age+1}살이 됩니다!")
# 이름과 나이를 입력받아서 출력하세요
# 홍길동님은 내년에 26살이 됩니다!

# 문제2()

def 문제3():
    점수 = int(input("점수를 입력하세요: "))
    if 점수 >= 90 :
        print("A학점")
    elif 점수 >= 80:
        print("B학점")
    elif 점수 >= 70 :
        print("C학점")
    else :
        print("F학점")
    # 90이상 A학점
    # 80이상 B학점
    # 70이상 C학점
    # 나머지 F학점

# 문제3()

def 문제4():
    total = 0
    while True:
        num = input("숫자를 입력하세요 (exit 종료): ")
        if num.lower() == "exit":
            break
        total += int(num)
    print(f"숫자들의 합계: {total}")
# 숫자를 입력받아서 exit 입력시 종료
# 입력한 숫자들의 합계 출력
# 합계: 60

# 문제4()

def 문제5():
    단 = int(input("단수를 입력하세요: "))
    for i in range(1,10):
        print(f"{단} X {i} = {단*i}")
    # 구구단 출력
    # 3 X 1 = 3
    # 3 X 2 = 6
    # ...

# 문제5()

def 문제6():
    과일들 = ["사과", "바나나", "포도"]
    과일들.append("수박")
    과일들.remove("바나나")
    print(과일들)
    과일개수 = len(과일들)
    print(f"과일개수 : {과일개수}개")
    # 수박 추가
    # 바나나 삭제
    # 전체 출력
    # 과일 개수 출력

# 문제6()

def 문제7():
    언어들 = ["Python", "Java", "JavaScript", "HTML", "CSS"]

    for 번호, 언어 in enumerate(언어들, start=1):
        print(f"{번호}번: {언어}")
    # enumerate 이용해서 1번부터 출력
    # 1번: Python
    # 2번: Java
    # ...

# 문제7()

def 문제8():
    파일이름 = input("파일 이름을 입력하세요: ")
    확장자 = input("확장자를 입력하세요: ")

    전체파일이름 = 파일이름+"."+확장자

    with open(전체파일이름, "w", encoding="utf-8") as file:
        while True:
            text = input("입력하세요 (exit 종료): ")
            if text.lower() == "exit":
                print(f"{전체파일이름}작성완료")
                break
            file.write(text + "\n")
# 파일이름과 확장자를 input으로 받아서
# exit 입력 전까지 내용 작성
# 작성완료 출력

# 문제8()

def 문제9():
    with open("실습문제.txt","r", encoding="utf-8") as file:
        파일내용 = file.readlines()

        for 번호, 내용 in enumerate(파일내용, start=1):
            print(f"{번호}번째 줄: {내용}")

# 문제8에서 만든 파일을
# 줄번호와 함께 읽기
# 1번째 줄: 내용
# 2번째 줄: 내용

# 문제9()

def 문제10():
    이름들 = []
    점수들 = []

    for i in range(3):
        이름 = input(f"{i+1}번째 이름을 입력하세요: ")
        점수 = int(input(f"{i+1}번째 점수를 입력하세요: "))
        이름들.append(이름)
        점수들.append(점수)

    for idx, 이름 in enumerate(이름들, start=1):
        점수 = 점수들[idx-1]
        print(f"{idx}번: {이름} - {점수}점")

    평균 = sum(점수들) / len(점수들)
    print(f"평균: {평균}점")
    # 이름 3개 + 점수 3개 입력받아서 리스트에 저장
    # enumerate 로 번호 붙여서 출력
    # 평균 점수 출력
    # 1번: 홍길동 - 90점
    # 2번: 김철수 - 80점
    # 3번: 이영희 - 70점
    # 평균: 80.0점

문제10()