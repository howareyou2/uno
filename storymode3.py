import pygame
import singlegame

pygame.init()

def story_map3():
    # 화면 크기, 색상 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    #배경화면에 이미지 띄우기
    back_image = pygame.image.load("./이채은/image/jeju.png")
    bird_image = pygame.image.load("./이채은/image/bird.png")
    bird_image = pygame.transform.scale(bird_image, (98,77))
    
    screen.fill((135, 206, 235))
    #배경 이미지 크기 조절 800, 600
    back_image = pygame.transform.scale(back_image, (800, 600))
    
    #back_image위에 './이채은/image/airport.png'이미지를 띄워놓기, 크기, 위치 조절
    
    airplane_image = pygame.image.load("./이채은/image/airport.png")
    airplane_image = pygame.transform.scale(airplane_image, (98,77))
    
    Hsan_image = pygame.image.load("./이채은/image/Hsan.png")
    Hsan_image = pygame.transform.scale(Hsan_image, (160,120))
    
    EU_image = pygame.image.load("./이채은/image/EU.png")
    EU_image = pygame.transform.scale(EU_image, (98,85))
    
    flower_image = pygame.image.load("./이채은/image/flower.png")
    flower_image = pygame.transform.scale(flower_image, (98,95))
    
    waterfall_image = pygame.image.load("./이채은/image/waterfall.png")
    waterfall_image = pygame.transform.scale(waterfall_image, (98,77))
    
    hae_image = pygame.image.load("./이채은/image/hae.png")
    hae_image = pygame.transform.scale(hae_image, (110,120))
    
    GG_image = pygame.image.load("./이채은/image/GG.png")
    GG_image = pygame.transform.scale(GG_image, (98,77))
    
    stone_image = pygame.image.load("./이채은/image/stone.png")
    stone_image = pygame.transform.scale(stone_image, (88,77))
    
    airplane_rect = airplane_image.get_rect()
    airplane_rect.center = (350, 178)
    
    Hsan_rect = Hsan_image.get_rect()
    Hsan_rect.center = (400, 270)
    
    EU_rect = EU_image.get_rect()
    EU_rect.center = (170, 260)
    
    flower_rect = flower_image.get_rect()
    flower_rect.center = (200, 450)
    
    waterfall_rect = waterfall_image.get_rect()
    waterfall_rect.center = (450, 440)
    
    hae_rect = hae_image.get_rect()
    hae_rect.center = (650, 140)
    
    stone_rect = stone_image.get_rect()
    stone_rect.center = (470, 290)
    
    screen.blit(back_image, (0,0))
    screen.blit(bird_image, (120, 50))
    screen.blit(airplane_image, airplane_rect)
    screen.blit(Hsan_image, Hsan_rect)
    screen.blit(EU_image, EU_rect)
    screen.blit(flower_image, flower_rect)
    screen.blit(waterfall_image, waterfall_rect)
    screen.blit(hae_image, hae_rect)
    screen.blit(stone_image, stone_rect)
    
    pygame.display.update()
    
    # 캐릭터 이미지 불러오기, 크기 설정
    char_img1 = pygame.image.load("./이채은/image/R1.png")
    char_img2 = pygame.image.load("./이채은/image/R2.png")
    char_img3 = pygame.image.load("./이채은/image/R3.png")
    char_img4 = pygame.image.load("./이채은/image/R4.png")
    char_img_list = [char_img1, char_img2, char_img3, char_img4]
    char_width, char_height = (40, 40)
    char_img_list = [pygame.transform.scale(img, (char_width, char_height)) for img in char_img_list]
    
    # 캐릭터의 위치, 속도 설정
    char_x, char_y = 240, 420
    char_speed = 0.2
    
    # 이동할 좌표
    move_x, move_y = 0,0
    
    # 캐릭터 이미지 인덱스, 이미지 변경 시간, 이미지 변경 시간 간격 설정
    char_img_index = 0
    change_img_time = 0
    change_img_interval = 90
    
    # 캐릭터가 바라보는 방향 설정 (오른쪽: 0, 왼쪽: 1)
    char_direction = 0
    
    #캐릭터가 이동할 수 있는 범위 설정, 원모양으로 설정
    char_range = 100
    char_range_x = 0
    char_range_y = 0
    
    ## 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            # 키가 눌렸는지 확인
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                #    move_x -= char_speed
                #    char_direction = 1  # 왼쪽으로 이동할 때 캐릭터 방향 변경
                #    char_img_index = 1  # 왼쪽으로 이동할 때 캐릭터 이미지 인덱스 변경
                if event.key == pygame.K_SPACE:
                    move_x += char_speed
                    char_direction = 0  # 오른쪽으로 이동할 때 캐릭터 방향 변경
                    char_img_index = 0  # 오른쪽으로 이동할 때 캐릭터 이미지 인덱스 변경
                #elif event.key == pygame.K_UP:
                #    move_y -= char_speed
                #elif event.key == pygame.K_DOWN:
                #    move_y += char_speed
    
            # 키가 떼졌는지 확인
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    move_x = 0
                    char_img_index = 0  # 이동 중이 아니므로 캐릭터 이미지 인덱스를 기본값으로 변경
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_y = 0
    
        # 캐릭터의 위치를 변경
        char_x += move_x
        char_y += move_y
    
    #캐릭터가 screen밖으로 못넘어가게 설정
    #    if char_x < 0:
    #        char_x = 0
    #    elif char_x > screen_width - char_width:
    #        char_x = screen_width - char_width
    #    if char_y < 0:
    #        char_y = 0
    #    elif char_y > screen_height - char_height:
    #        char_y = screen_height - char_height
    #
    #    # 캐릭터가 이동할때 전 위치를 지우고 새로운 위치에 그림
    #    
        screen.blit(back_image, (char_x, char_y), (char_x, char_y, char_width, char_height))
    #
        # 캐릭터 이미지 변경
        if move_x != 0:
            if pygame.time.get_ticks() - change_img_time >= change_img_interval:
                char_img_index += 1
                if char_img_index >= len(char_img_list):
                    char_img_index = 0
                change_img_time = pygame.time.get_ticks()
    
        # 화면에 그리기
        if move_x > 0:  # 캐릭터가 오른쪽으로 이동중인 경우
            screen.blit(char_img_list[char_img_index], (char_x, char_y))
     #   elif move_x < 0:  # 캐릭터가 왼쪽으로 이동중인 경우
     #       flipped_char_img = pygame.transform.flip(char_img_list[char_img_index], True, False)
     #       screen.blit(flipped_char_img, (char_x, char_y))
        else:  # 캐릭터가 이동하지 않고 멈춰있는 경우
            if char_direction == 0:  # 오른쪽을 보고 있는 경우
                screen.blit(char_img_list[0], (char_x, char_y))
    #        else:  # 왼쪽을 보고 있는 경우
    #            flipped_char_img = pygame.transform.flip(char_img_list[0], True, False)
    #            screen.blit(flipped_char_img, (char_x, char_y))
        #defining waterfall_x, waterfall_y, waterfall_width, waterfall_height
        waterfall_x = 400
        waterfall_y = 400
        waterfall_width = 98
        waterfall_height = 77
    #font
        font = pygame.font.SysFont('comicsans', 20)
    #캐릭터와 waterfall이 충돌하면 캐릭터의 위치가 멈추게 설정, waterfall위에 텍스트 출력
        if char_x + char_width > waterfall_x and char_x < waterfall_x + waterfall_width and char_y + char_height > waterfall_y and char_y < waterfall_y + waterfall_height:
            char_x -= move_x
            char_y -= move_y
            waterfall_text = font.render("Waterfall: ENTER!", True, (0, 0, 0))
            screen.blit(waterfall_text, (waterfall_x, waterfall_y - 20))
    
            #defining mouse_x, mouse_y
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
            #waterfall이미지와 충돌 후 엔터를 누르면 singlegame으로 넘어가게 설정
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    singlegame.start_game()
    
            pygame.display.update()
        pygame.display.update()