import pygame
import sys
import pause

pygame.init()

def start_game():

    #'배경1.mp3' 파일 재생
    pygame.mixer.music.load('./이채은/sound/배경1.mp3')
    pygame.mixer.music.play(-1)

    # 전체화면 설정
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("UNO Game")

    # 색 정의
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    LIGHT_PINK = (255, 182, 193)
    GRAY = (128, 128, 128)
    RED = (255, 0, 0)
    LIGHT_YELLOW = (255, 255, 153)

    #섹션1 크기, 테두리 설정, 배경사진'background.png'
    section1_width = int(screen_width*0.80)
    section1_height = int(screen_height*0.60)
    section1 = pygame.Surface((section1_width, section1_height))

    background = pygame.image.load('./이채은/image/singleBG_c.png')
    background = pygame.transform.scale(background, (section1_width, section1_height))
    section1.blit(background, (0, 0, 10, 10))
    pygame.draw.rect(section1, LIGHT_YELLOW, (0, 0, section1_width, section1_height), 3)

    #섹션1 왼쪽에 'BACK.png' 이미지 띄우기
    back = pygame.image.load('./최회민/img/BACK.png')
    back = pygame.transform.scale(back, (int(section1_width*0.20), int(section1_height*0.45)))
    section1.blit(back, (120, 110, 10, 10))

    #'BACK.png' 이미지 누르면 ~기능 구현?

    # 현재 색 표시 칸 구현
    pygame.draw.circle(section1, WHITE, (int(section1_width*0.8), int(section1_height*0.45)), int(section1_width*0.05), 0)
    pygame.draw.circle(section1, LIGHT_YELLOW, (int(section1_width*0.8), int(section1_height*0.45)), int(section1_width*0.05), 3)

    # 색 표시 기능 구현

    #섹션2 크기, 배경색, 테두리 설정
    section2_width = int(screen_width*0.25)
    section2_height = screen_height
    section2 = pygame.Surface((section2_width, section2_height))
    section2.fill((LIGHT_YELLOW))
    pygame.draw.rect(section2, LIGHT_YELLOW, (0, 0, section2_width, section2_height), 3)

    #플레이어별 위치 구현
    p_width = int(section2_width / 1.0) # Width of each rectangle, slightly smaller than section2
    p_height = int((section2_height - 10) / 6) # Height of each rectangle, spaced apart by 2
    p_spacing = 3 # Spacing between rectangles

    p1_rect = pygame.Rect((section2_width - p_width) / 2, p_spacing, p_width*0.789, p_height)
    p2_rect = pygame.Rect((section2_width - p_width) / 2, p_height + p_spacing * 2, p_width*0.789, p_height)
    p3_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 2 + p_spacing * 3, p_width*0.789, p_height)
    p4_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 3 + p_spacing * 4, p_width*0.789, p_height)
    p5_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 4 + p_spacing * 5, p_width*0.789, p_height)
    p6_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 5 + p_spacing * 6, p_width*0.789, p_height)

    #p에 모두 'se2.png' 이미지 띄우기
    se2 = pygame.image.load('./이채은/image/se2.png')
    se2 = pygame.transform.scale(se2, (int(p_width*0.789), int(p_height)))
    section2.blit(se2, (p1_rect.x, p1_rect.y, 10, 10))
    section2.blit(se2, (p2_rect.x, p2_rect.y, 10, 10))
    section2.blit(se2, (p3_rect.x, p3_rect.y, 10, 10))
    section2.blit(se2, (p4_rect.x, p4_rect.y, 10, 10))
    section2.blit(se2, (p5_rect.x, p5_rect.y, 10, 10))
    section2.blit(se2, (p6_rect.x, p6_rect.y, 10, 10))


#섹션2 플레이어별 이름 표시
    font = pygame.font.SysFont('comicsansms', 18)
    text = font.render('Player1', True, BLACK)
    section2.blit(text, (p1_rect.x + 10, p1_rect.y + 10, 10, 10))
    text = font.render('Player2', True, BLACK)
    section2.blit(text, (p2_rect.x + 10, p2_rect.y + 10, 10, 10))
    text = font.render('Player3', True, BLACK)
    section2.blit(text, (p3_rect.x + 10, p3_rect.y + 10, 10, 10))
    text = font.render('Player4', True, BLACK)
    section2.blit(text, (p4_rect.x + 10, p4_rect.y + 10, 10, 10))
    text = font.render('Player5', True, BLACK)
    section2.blit(text, (p5_rect.x + 10, p5_rect.y + 10, 10, 10))
    text = font.render('Player6', True, BLACK)
    section2.blit(text, (p6_rect.x + 10, p6_rect.y + 10, 10, 10))

    #섹션3 크기, 배경색, 테두리 설정
    section3_width = section1_width
    section3_height = int(screen_height*0.40)
    section3 = pygame.Surface((section3_width, section3_height))
    section3.fill((255, 255, 255))
    pygame.draw.rect(section3, LIGHT_YELLOW, (0, 0, section3_width, section3_height), 3)

    #섹션3 우측 상단에 타이머 표시 칸 구현
    timer_width = int(section3_width*0.05)
    timer_height = int(section3_height*0.25)
    timer_x = section3_width - timer_width - 15
    timer_y = 10

    #섹션3 우측 상단에 타이머 표시 칸 안에 "0" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("0", True, RED)
    text_rect = text.get_rect(center=(timer_x + timer_width / 2, timer_y + timer_height / 2))
    section3.blit(text, text_rect)

#섹션3 좌측 상단에 "Your turn" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    text = font.render("Your turn", True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width*0.1), int(section3_height*0.1)))
    section3.blit(text, text_rect)

    #"UNO!" 텍스트 생성
    font = pygame.font.SysFont('comicsansms', 20)
    bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
    text = font.render("UNO!", True, BLACK)
    text_rect = text.get_rect(center=(int(section3_width*0.23), int(section3_height*0.1)))
    pygame.draw.rect(section3, RED, (text_rect.x - 5, text_rect.y - 5, text_rect.width + 10, text_rect.height + 10), 3)
    section3.blit(text, text_rect)

    ##섹션3 우측 중앙에 마지막 한장 남았을때 누르는 버튼 구현
    #UNO_bt = pygame.image.load('./이채은/image/UNO_bt.png')
    #UNO_bt = pygame.transform.scale(UNO_bt, (150,110))
    #section3.blit(UNO_bt, (int(section3_width*0.72), int(section3_height*0.2), 10, 10))

    # 일시정지 및 종료 버튼 구현하고 "Pause" 텍스트 생성
    pause_button = pygame.Rect(10, 10, 30, 30)
    pygame.draw.rect(section1, LIGHT_YELLOW, pause_button)

    def draw_game_screen():
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, LIGHT_PINK, pause_button)

        screen.blit(section1, (0, 0))
        screen.blit(section2, (section1_width, 0))
        screen.blit(section3, (0, section1_height))
        pygame.display.update()

    def draw_pause_screen():
        pause.run_pause_screen(screen)

    def resume_game():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        return False
    
    # 게임 루프
    running = True
    paused = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 마우스 왼쪽 버튼 클릭 시 pause 버튼을 누른 것으로 인식합니다.
                if pause_button.collidepoint(event.pos) and not paused:
                    paused = True
    
        # 게임 일시정지
        if paused:
            draw_pause_screen()  # pause.py의 run_pause_screen() 함수를 실행합니다.
        else:
            draw_game_screen()  # 게임 화면을 그립니다.

        if paused and resume_game():
            paused = False



    pygame.display.flip()




    pygame.display.flip()
