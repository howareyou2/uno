수정한 새코드

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


#섹션을 세개로 나눠 각각의 크기를 지정, 배경색을 설정
section1_width = int(screen_width*0.75)
section1_height = int(screen_height*0.67)
section1 = pygame.Surface((section1_width, section1_height))
section1.fill((0, 0, 0))

section2_width = int(screen_width*0.25)
section2_height = section1_height
section2 = pygame.Surface((section2_width, section2_height))
section2.fill((255, 0, 0))

section3_width = screen_width
section3_height = int(screen_height*0.33)
section3 = pygame.Surface((section3_width, section3_height))
section3.fill((0, 255, 0))

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
font = pygame.font.SysFont("Arial", 10)

# 게임 루프 실행
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 버튼 클릭 시 팝업창 띄우기
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
 
            # 팝업창 크기 지정
            popup_width = 200
            popup_height = 150
            popup_x = int((screen_width - popup_width) / 2)
            popup_y = int((screen_height - popup_height) / 2)
            
            #팝업창 폰트 지정
            font = pygame.font.SysFont("Arial", 20)

            # 팝업창 배경색 지정
            popup = pygame.Surface((popup_width, popup_height))
            popup.fill((0, 0, 0))

            #팝업창 흰색 테두리 지정
            pygame.draw.rect(popup, WHITE, (0, 0, popup_width, popup_height), 5)

            #팝업창 "X"버튼을 지정하고 배경색은 흰색으로 지정,글씨는 흰색으로 지정,  누르면 팝업창이 닫히게 함
            x_button = pygame.draw.rect(popup, WHITE, (popup_width - 30, 10, 20, 20))
            x_text = font.render("X", True, BLACK)
            popup.blit(x_text, (popup_width - 25, 10))

            #팝업창 "X"버튼을 누르면 팝업창이 닫히게 함
            if event.type == pygame.MOUSEBUTTONDOWN and x_button.collidepoint(event.pos):
                break

            # 팝업창에 "일시정지"와 "종료" 버튼 만들기
            pause_button = pygame.draw.rect(popup, WHITE, (int(popup_width / 2) - 50, int(popup_height / 2) - 50, 100, 30))
            exit_button = pygame.draw.rect(popup, WHITE, (int(popup_width / 2) - 50, int(popup_height / 2) - 10, 100, 30))
            
            # 팝업창에 "일시정지"와 "종료" 글씨 쓰기
            pause_text = font.render("Pause", True, BLACK)
            exit_text = font.render("EndGame", True, BLACK)
            popup.blit(pause_text, (int(popup_width / 2) - 30, int(popup_height / 2) - 45))
            popup.blit(exit_text, (int(popup_width / 2) - 35, int(popup_height / 2) - 5))

            # 팝업창 띄우기
            screen.blit(popup, (popup_x, popup_y))


 #           # 팝업창에 "Pause" 버튼 클릭 시 일시정지, "End Game" 버튼 클릭 시 'startPage.py'로 돌아가기
 #           while True:
 #               for event in pygame.event.get():
 #                   if event.type == pygame.QUIT:
 #                       pygame.quit()
 #                       sys.exit()
 #                   if event.type == pygame.MOUSEBUTTONDOWN and pause_button.collidepoint(event.pos):
 #                       break
 #                   if event.type == pygame.MOUSEBUTTONDOWN and exit_button.collidepoint(event.pos):
 #                       os.system("startPage.py")
 #                       break




            pygame.display.flip()
