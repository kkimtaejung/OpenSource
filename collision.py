import pygame

# 기본 초기화 (반드시 지정해 두어야함)
####################################################################
pygame.init() # 초기화



# FPS
clock = pygame.time.Clock()

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = (character_height / 2) # 화면 세로의 절반 크기에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1


import tkinter
tk = tkinter.Tk()

canvas = tkinter.Canvas(width = 500, height = 350, bg = "white")
canvas.pack()

gameMap = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
for y in range(7):
    for x in range(10):
        if gameMap[y][x] == 1:
            canvas.create_rectangle(x *50, y*50, x*50+50, y*50+50, fill="yellow")

tk.mainloop()

cnt = 0

running = True # 게임이 진행중인가? True = 그렇다.
while running: # True면 계속 while문 반복해라!
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # pygame만들기 위해 무조건 적어야하는 식 ( 어떠 이벤트가 발생했는가? )
        if event.type == pygame.QUIT: # x표시로 창을 껐을 때 즉, 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 탈출

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        # 방향키를 뗐을 때 0이 더해지기 때문에 제자리에 머문다.

        character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리  
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos >character_width:
        character_x_pos = character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos >character_height:
        character_y_pos =character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    if character_rect.colliderect():
        print("충돌했어요")
        running = False

    gameMap.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 

    pygame.display.update() # 게임화면을 다시 그리기 ( 계속 화면을 그려줌 )

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()
