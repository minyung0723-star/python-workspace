'''
python 으로 가볍게 게임을 만드는 라이브러리

화면에 도형/이미지 그리기
키보드/마우스 실시간 감지
소리 재생
애니메이션

설치방법 pip install pygame
'''
import pygame

# pygame.init() #pygame. 초기세팅
# 화면 = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("나의 게임")
# 시계 = pygame.time.Clock()
#
# # 게임 루프 (Tkinter의 mainloop 같은 것_
# 실행중 = True
# while 실행중:
#     # 1. 이벤트 처리
#     for 이벤트 in pygame.event.get():
#         if 이벤트.type == pygame.QUIT: # x버튼을 마우스로 클릭하면
#             실행중 = False
#
#     # 2. 화면 그리기
#     화면.fill((0,0,0))            # 화면 배경색 ( R, G, B) 255,255,255 black
#     pygame.display.flip()         # 화면 갱신
#
#     시계.tick(60) # 초당 60 프레임
#
# pygame.quit()

pygame.init() #pygame. 초기세팅
화면 = pygame.display.set_mode((800, 600))
pygame.display.set_caption("공 움직이기")
시계 = pygame.time.Clock()

# 공 초기 설정
공_x = 400
공_y = 300
공크기 = 20
속도 = 5
# 튜플 형태로 해서 흰색 컬러 추후 변경 불가하게 값 설정
흰색 = (255, 255, 255)
검정 = (0, 0, 0)
빨강 = (255, 0, 0)

# 게임 루프 (Tkinter의 mainloop 같은 것_
실행중 = True
while 실행중:
    # 1. 이벤트 처리
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT: # x버튼을 마우스로 클릭하면
            실행중 = False

    # 키보드 입력으로 공 이동
    키 = pygame.key.get_pressed()
    if 키[pygame.K_LEFT]: 공_x -= 속도
    if 키[pygame.K_RIGHT]: 공_x += 속도
    if 키[pygame.K_UP]: 공_y -= 속도
    if 키[pygame.K_DOWN]: 공_y += 속도

    # 벽 충돌(화면 밖으로 공이 나가지 못하게
    공_x = max(공크기, min(800-공크기,공_x))
    공_y = max(공크기, min(600-공크기,공_y))

    # 2. 화면 그리기
    화면.fill(검정)            # 화면 배경색 ( R, G, B) 255,255,255 black
    pygame.draw.circle(화면,빨강,(공_x,공_y), 공크기)
    pygame.display.flip()         # 화면 갱신

    시계.tick(60) # 초당 60 프레임

pygame.quit()