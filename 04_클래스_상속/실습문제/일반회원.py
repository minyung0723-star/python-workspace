from 회원 import 회원

# 6. 상속 - () 안에 부모 클래스 작성
class 일반회원(회원):

    # 추가 메서드
    def 혜택안내(self):
        print(f"{self.이름}님의 혜택: 기본 적립 1%")