class 사람:
    종족 = "휴먼"

    def __init__(self, 이름, 나이):
        self.이름 = 이름
        self.나이 = 나이

    def 소개(self):
        print(f"이름 : {self.이름}, 나이:{self.나이}, 종족:{사람.종족}")

A군= 사람("철수",25)
B군= 사람("영희",20)
C군= 사람("민준",23)

print(A군.이름)
print(B군.이름)

print(A군.종족)
print(B군.종족)
print(C군.종족)

A군.소개();
B군.소개();

사람.종족 = "인간"

print(A군.종족)
print(B군.종족)
print(C군.종족)
