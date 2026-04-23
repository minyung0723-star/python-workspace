import datetime

def 현재시간():
    지금 = datetime.datetime.now()
    return f"{지금.hour}:{지금.minute:02d}"

def 단체전송(*받는사람들, 메세지, 타입="text"):
    for 사람 in 받는사람들:
        print(f"{사람}에게 {타입}로 {메세지} 전송")
# 받는사람들 한명씩 꺼내서
# "{사람}에게 {타입}로 {메세지} 전송" 출력하기