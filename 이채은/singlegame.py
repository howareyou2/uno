import pygame
import sys
import os


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
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


#섹션을 세개로 나눠 각각의 크기, 배경색, 테두리 설정
section1_width = int(screen_width*0.75)
section1_height = int(screen_height*0.67)
section1 = pygame.Surface((section1_width, section1_height))
section1.fill((0, 0, 0))
pygame.draw.rect(section1, WHITE, (0, 0, section1_width, section1_height), 3)

section2_width = int(screen_width*0.25)
section2_height = section1_height
section2 = pygame.Surface((section2_width, section2_height))
section2.fill((255, 0, 0))
pygame.draw.rect(section2, WHITE, (0, 0, section2_width, section2_height), 3)

section3_width = screen_width
section3_height = int(screen_height*0.33)
section3 = pygame.Surface((section3_width, section3_height))
section3.fill((0, 255, 0))
pygame.draw.rect(section3, WHITE, (0, 0, section3_width, section3_height), 3)

# 일시정지 및 종료 버튼 구현하고 "Pause" 텍스트를 띄우기
button_width = 50
button_height = 30
button_x = section1_width - button_width - 10
button_y = 10

WHITE = (255, 255, 255)
button_rect = pygame.draw.rect(section1, WHITE, (button_x, button_y, button_width, button_height))

screen.blit(section1, (0, 0))
screen.blit(section2, (section1_width, 0))
screen.blit(section3, (0, section1_height))

# 버튼 텍스트 지정
font = pygame.font.SysFont("Arial", 20)
button_text = font.render("Pause", True, BLACK)
button_text_rect = button_text.get_rect(center=(button_x + button_width / 2, button_y + button_height / 2))
screen.blit(button_text, button_text_rect)


pygame.display.flip()

# 팝업창 폰트 지정
font = pygame.font.SysFont("Arial", 20)

# 게임 루프 실행
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

         # "Pause" 버튼 클릭 시 팝업창 띄우기
        elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):

            # 팝업창 크기 지정
            popup_width = 200
            popup_height = 150
            popup_x = int((screen_width - popup_width) / 2)
            popup_y = int((screen_height - popup_height) / 2)
            
            # 팝업창 배경색 지정
            popup = pygame.Surface((popup_width, popup_height))
            popup.fill((255, 255, 255))

            #팝업창 테두리 지정
            pygame.draw.rect(popup, WHITE, (0, 0, popup_width, popup_height), 5)

            #"X"버튼
            x_button = pygame.draw.rect(popup, WHITE, (popup_width - 30, 10, 20, 20))
            x_text = font.render("X", True, BLACK)
            popup.blit(x_text, (popup_width - 25, 10))

            #"X"버튼 클릭 시 팝업창 종료
            if event.type == pygame.MOUSEBUTTONDOWN and x_button.collidepoint(event.pos):
                pygame.quit()
                sys. exit()

            # 팝업창에 "초기화","게임종료"버튼, 배경색 지정
            reset_button = pygame.draw.rect(popup, WHITE, (int(popup_width / 2) - 50, int(popup_height / 2) - 50, 100, 40))
            exit_button = pygame.draw.rect(popup, WHITE, (int(popup_width / 2) - 50, int(popup_height / 2) - 10, 100, 40))

            # 팝업창에 "Reset"와 "EndGame" 글씨 쓰기
            reset_text = font.render("Reset", True, BLACK)
            exit_text = font.render("EndGame", True, BLACK)
            popup.blit(reset_text, (int(popup_width / 2) - 30, int(popup_height / 2) - 45))
            popup.blit(exit_text, (int(popup_width / 2) - 35, int(popup_height / 2) - 5))

            # 팝업창 띄우기
            screen.blit(popup, (popup_x, popup_y))

            pygame.display.flip()
    pygame.display.flip()
