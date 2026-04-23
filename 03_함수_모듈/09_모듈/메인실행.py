# import 계산기 # 모듈을 가져와서 사용하겠다.
# print(계산기.더하기(10,5))
# from 계산기 import 빼기 # 계산기. 을 붙이지 않고 빼기 기능을 사용하겠다.
# print(빼기(10,6))

import 시간
import 메세지

while True:
    내용 = input("나 : ")

    if 내용 == "종료":
        print("채팅을 종료합니다.")
        break

    지금 = 시간.현재시간()
    메세지.메세지보내기("나", 내용, 지금)