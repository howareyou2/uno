import pygame
import sys

pygame.init()

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
section2_height = section1_height
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
p6_rect = pygame.Rect((section2_width - p_width) / 2, p_height * 5 + p_spacing * 6, p_width*0.789, p_height*0.87)

#p에 모두 'se2.png' 이미지 띄우기
se2 = pygame.image.load('./이채은/image/se2.png')
se2 = pygame.transform.scale(se2, (int(p_width*0.789), int(p_height)))
section2.blit(se2, (p1_rect.x, p1_rect.y, 10, 10))
section2.blit(se2, (p2_rect.x, p2_rect.y, 10, 10))
section2.blit(se2, (p3_rect.x, p3_rect.y, 10, 10))
section2.blit(se2, (p4_rect.x, p4_rect.y, 10, 10))
section2.blit(se2, (p5_rect.x, p5_rect.y, 10, 10))
section2.blit(se2, (p6_rect.x, p6_rect.y, 10, 10))

#섹션3 크기, 배경색, 테두리 설정
section3_width = screen_width
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

#섹션3 우측 중앙에 마지막 한장 남았을때 누르는 버튼 구현
UNO_bt = pygame.image.load('./이채은/image/UNO_bt.png')
UNO_bt = pygame.transform.scale(UNO_bt, (150,110))
section3.blit(UNO_bt, (int(section3_width*0.72), int(section3_height*0.2), 10, 10))

# 일시정지 및 종료 버튼 구현하고 "Pause" 텍스트 생성
pause_button_width = 50
pause_button_height = 30
pause_button_x = section1_width - pause_button_width - 10
pause_button_y = 10

#"pause_button"배경 흰색으로 설정
WHITE = (255, 255, 255)
pause_button_rect = pygame.draw.rect(section1, LIGHT_YELLOW, (pause_button_x, pause_button_y, pause_button_width, pause_button_height), border_radius=10)

font = pygame.font.SysFont('comicsansms', 15)
bold_font = pygame.font.SysFont('comicsansms', 15, bold=True)
text = font.render("Pause", True, BLACK)
text_rect = text.get_rect(center=(pause_button_x + pause_button_width / 2, pause_button_y + pause_button_height / 2))
section1.blit(text, text_rect)

screen.blit(section1, (0, 0))
screen.blit(section2, (section1_width, 0))
screen.blit(section3, (0, section1_height))

pygame.display.flip()

# 팝업창 폰트 지정
font = pygame.font.SysFont('comicsansms', 20)

# 게임 루프 실행
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #"pause"버튼을 누르면 '배경.mp3'가 멈춘다.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
                pygame.mixer.music.rewind()
                pygame.display.update()

        #"Pause" 버튼을 누르면 게임이 일시정지
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button_rect.collidepoint(event.pos):
                pygame.time.wait(1000)
                pygame.display.update()

                #"Pause" 버튼을 누르면 "Continue", "Restart", "EndGame" 버튼 생성
                pygame.draw.rect(screen, WHITE, (300, 230, 180, 40))
                pygame.draw.rect(screen, WHITE, (300, 275, 180, 40))
                pygame.draw.rect(screen, WHITE, (300, 320, 180, 40))


                #각각의 버튼에 "Continue", "Restart", "EndGame" 텍스트 생성
                co_text = font.render("Continue", True, BLACK)
                co_text_rect = co_text.get_rect(center=(300 + 150 / 2, 230 + 40 / 2))
                screen.blit(co_text, co_text_rect)

                re_text = font.render("Restart", True, BLACK)
                re_text_rect = re_text.get_rect(center=(300 + 165 / 2, 275 + 40 / 2))
                screen.blit(re_text, re_text_rect)

                ex_text = font.render("EndGame", True, BLACK)
                ex_text_rect = ex_text.get_rect(center=(300 + 140 / 2, 320 + 40 / 2))
                screen.blit(ex_text, ex_text_rect)

                pygame.display.flip()
                
            #ex_text를 누르면 게임이 종료되고 'startPage.py'로 돌아감
            if ex_text_rect.collidepoint(event.pos):
                import startPage
                startPage.startPage()

            #re_text를 누르면 'singlegame.py'가 다시 실행
            if re_text_rect.collidepoint(event.pos):
                import singlegame
                singlegame.singlegame()

            #co_text를 누르면 ex_text, re_text, co_text가 닫히고 '배경.mp3'가 다시 실행되며 게임이 이어서 진행됨
            #계속 수정..
            if co_text_rect.collidepoint(event.pos):
                pygame.draw.rect(screen, (255, 255, 0), (300, 230, 180, 40))
                pygame.draw.rect(screen, (255, 255, 0), (300, 275, 180, 40))
                pygame.draw.rect(screen, (255, 255, 0), (300, 320, 180, 40))
                pygame.mixer.music.unpause()
                pygame.display.flip()

            pygame.display.flip() 
