import pygame
import sys

pygame.init()

# 전체화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("UNO Game")

# 색 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 섹션 크기, 배경색 정의(임의로 한거임..니다^^)
section1_width = int(screen_width * 0.75)
section1_height = int(screen_height * 0.67)
section2_width = int(screen_width * 0.25)
section2_height = section1_height
section3_width = screen_width
section3_height = int(screen_height * 0.33)

section1 = pygame.Surface((section1_width, section1_height))
section1.fill(RED)
section2 = pygame.Surface((section2_width, section2_height))
section2.fill(BLACK)
section3 = pygame.Surface((section3_width, section3_height))
section3.fill(GREEN)

# 일시정지 및 종료 버튼 구현
button_width = 30
button_height = 30
button_x = section1_width - button_width - 10
button_y = 10

WHITE = (255, 255, 255)
button_rect = pygame.draw.rect(section1, WHITE, (button_x, button_y, button_width, button_height))

screen.blit(section1, (0, 0))
screen.blit(section2, (section1_width, 0))
screen.blit(section3, (0, section1_height))

pygame.display.flip()

# 팝업창 폰트 지정
font = pygame.font.SysFont("Arial", 20)

# 게임 루프 실행
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 흰 버튼 클릭하면
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            # 팝업 창 생성
            popup_width = 300
            popup_height = 200
            popup_surface = pygame.Surface((popup_width, popup_height))
            popup_surface.fill(WHITE)

            # 팝업창에 "Pause" 와 "End Game" 버튼 추가
            pause_button_rect = pygame.draw.rect(popup_surface, RED, (50, 50, 80, 40))
            end_button_rect = pygame.draw.rect(popup_surface, RED, (170, 50, 80, 40))
            pause_text = font.render("Pause", True, BLACK)
            end_text = font.render("End Game", True, BLACK)
            popup_surface.blit(pause_text, (60, 60))
            popup_surface.blit(end_text, (180, 60))

            # 팝업 창 닫기 버튼
            close_button_rect = pygame.draw.rect(popup_surface, BLACK, (popup_width - 30, 10, 20, 20))
            close_text = font.render("X", True, WHITE)
            popup_surface.blit(close_text, (popup_width - 23, 10))

            # 팝업 창 표시
            popup_x = int((screen_width - popup_width) / 2)
            popup_y = int((screen_height - popup_height) / 2)
            screen.blit(popup_surface, (popup_x, popup_y))

        # 팝업 창 종료버튼 누르면..이거 안되서 하는즁...
        if event.type == pygame.MOUSEBUTTONDOWN and close_button_rect.collidepoint(event.pos):
            popup_surface.fill(BLACK)
            screen.blit(popup_surface, (popup_x, popup_y))
            pygame.display.flip()

    pygame.display.flip()
