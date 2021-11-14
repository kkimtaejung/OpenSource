import pygame
import random

# 기본 초기화 (반드시 지정해 두어야함)
####################################################################
pygame.init() # 초기화

#화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 780 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("P A C M A N") # 게임 이름

# FPS
clock = pygame.time.Clock()
####################################################################


# 배경 이미지 불러오기
background = pygame.image.load("./background3.png")

# 캐릭터 (스프라이트) 불러오기
character = pygame.image.load("./character_R.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = (screen_width /2 ) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = (screen_height /2) - (character_height / 2) # 화면 세로의 절반 크기에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 enermy 캐릭터
enemy = pygame.image.load("./enemy1.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width =  enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width/10) - enemy_width
enemy_y_pos = (screen_height/10) - enemy_height
enemy_x_speed = random.randint(-5, 5)
enemy_y_speed = random.randint(-5, 5)

enemy2 = pygame.image.load("./enemy2.png")
enemy2_size = enemy2.get_rect().size # 이미지의 크기를 구해옴
enemy2_width =  enemy2_size[0] # 캐릭터의 가로 크기
enemy2_height = enemy2_size[1] # 캐릭터의 세로 크기
enemy2_x_pos = screen_width - enemy2_width
enemy2_y_pos = (screen_height/10) - enemy2_height
enemy2_x_speed = random.randint(-5, 5)
enemy2_y_speed = random.randint(-5, 5)

enemy3 = pygame.image.load("./enemy3.png")
enemy3_size = enemy3.get_rect().size # 이미지의 크기를 구해옴
enemy3_width =  enemy3_size[0] # 캐릭터의 가로 크기
enemy3_height = enemy3_size[1] # 캐릭터의 세로 크기
enemy3_x_pos = (screen_width/10) - enemy3_width
enemy3_y_pos = screen_height - enemy3_height
enemy3_x_speed = random.randint(-5, 5)
enemy3_y_speed = random.randint(-5, 5)

enemy4 = pygame.image.load("./enemy4.png")
enemy4_size = enemy4.get_rect().size # 이미지의 크기를 구해옴
enemy4_width =  enemy4_size[0] # 캐릭터의 가로 크기
enemy4_height = enemy4_size[1] # 캐릭터의 세로 크기
enemy4_x_pos = screen_width - enemy4_width
enemy4_y_pos = screen_height - enemy4_height
enemy4_x_speed = random.randint(-5, 5)
enemy4_y_speed = random.randint(-5, 5)

coin = pygame.image.load("./coin.png")
coin_size = coin.get_rect().size
coin_width = coin_size[0]
coin_height = coin_size[1]
coin_x_pos = random.randint(coin_width, screen_width - coin_width)
coin_y_pos = random.randint(coin_height, screen_height - coin_height)


#Font 정의
game_font = pygame.font.Font(None, 40)


#################################################################
# 2. 이벤트 처리 ( 키보드, 마우스 등 )

# 이벤트 루프 (창이 꺼지지 않게하기 위함)
cnt = 0
i = 0

running = True # 게임이 진행중인가? True = 그렇다.
while running: # True면 계속 while문 반복해라!
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정


    cnt += 1
    if cnt > 60:
        enemy_x_speed = random.randint(-5, 5)
        enemy_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy2_x_speed = random.randint(-5, 5)
        enemy2_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy3_x_speed = random.randint(-5, 5)
        enemy3_y_speed = random.randint(-5, 5)
        cnt = 0

    cnt += 1
    if cnt > 60:
        enemy4_x_speed = random.randint(-5, 5)
        enemy4_y_speed = random.randint(-5, 5)
        cnt = 0

    for event in pygame.event.get(): # pygame만들기 위해 무조건 적어야하는 식 ( 어떠 이벤트가 발생했는가? )
        if event.type == pygame.QUIT: # x표시로 창을 껐을 때 즉, 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 탈출

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - 5
                character = pygame.image.load("./character_L.png")
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
                character = pygame.image.load("./character_R.png")
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
                character = pygame.image.load("./character_U.png")
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed
                character = pygame.image.load("./character_D.png")

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        # 방향키를 뗐을 때 0이 더해지기 때문에 제자리에 머문다.
#################################################################

# 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리  
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width



    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 적 위치 정의

    enemy_x_pos += enemy_x_speed
    enemy_y_pos += enemy_y_speed

    enemy2_x_pos += enemy2_x_speed
    enemy2_y_pos += enemy2_y_speed

    enemy3_x_pos += enemy3_x_speed
    enemy3_y_pos += enemy3_y_speed

    enemy4_x_pos += enemy4_x_speed
    enemy4_y_pos += enemy4_y_speed

    
    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = screen_width - enemy_width

    if enemy_y_pos < 0:
        enemy_y_pos = 0
    elif enemy_y_pos > screen_width - enemy_width:
        enemy_y_pos = screen_width - enemy_width

    if enemy2_x_pos < 0:
        enemy2_x_pos = 0
    elif enemy2_x_pos > screen_width - enemy2_width:
        enemy2_x_pos = screen_width - enemy2_width

    if enemy2_y_pos < 0:
        enemy2_y_pos = 0
    elif enemy2_y_pos > screen_width - enemy2_width:
        enemy2_y_pos = screen_width - enemy2_width

    if enemy3_x_pos < 0:
        enemy3_x_pos = 0
    elif enemy3_x_pos > screen_width - enemy3_width:
        enemy3_x_pos = screen_width - enemy3_width

    if enemy3_y_pos < 0:
        enemy3_y_pos = 0
    elif enemy3_y_pos > screen_width - enemy3_width:
        enemy3_y_pos = screen_width - enemy3_width

    if enemy4_x_pos < 0:
        enemy4_x_pos = 0
    elif enemy4_x_pos > screen_width - enemy4_width:
        enemy4_x_pos = screen_width - enemy4_width

    if enemy4_y_pos < 0:
        enemy4_y_pos = 0
    elif enemy4_y_pos > screen_width - enemy4_width:
        enemy4_y_pos = screen_width - enemy4_width


################################################################

# 4. 충돌 처리

    # 충돌 처리를 위한 rect 정보 업데이트

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_x_pos
    enemy4_rect.top = enemy4_y_pos
    
    coin_rect = coin.get_rect()
    coin_rect.left = coin_x_pos
    coin_rect.top = coin_y_pos

    

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"

    if character_rect.colliderect(enemy2_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"

    if character_rect.colliderect(enemy3_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"


    if character_rect.colliderect(enemy4_rect):
        print("충돌했어요")
        running = False
        game_result = "Game Over"


    if character_rect.colliderect(coin_rect):
        print("100점 추가")
        i += 100
        coin_x_pos = random.randint(coin_width, screen_width - coin_width)
        coin_y_pos = random.randint(coin_height, screen_height - coin_height)
        screen.blit(coin, (coin_x_pos, coin_y_pos))


        


    

################################################################

# 5. 화면에 그리기

    screen.blit(background, (0, 0)) # 화면 맨 왼쪽 위를 원점으로 시작, 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos)) # 적 그리기
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos)) # 적 그리기
    screen.blit(enemy4, (enemy4_x_pos, enemy4_y_pos)) # 적 그리기
    screen.blit(coin, (coin_x_pos, coin_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기 ( 계속 화면을 그려줌 )

# 게임 오버&점수 메세지
game_result = "Game Over ! Final Score : %d " %i

msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width /2) , int(screen_height / 2)))
screen.blit(msg, msg_rect)


pygame.display.update() # 게임화면을 다시 그리기 ( 계속 화면을 그려줌 )

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()


