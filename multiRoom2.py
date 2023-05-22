import pygame
from pygame.locals import *
import ipAdressInput2
#import server
import lobbyforServer
#import game_logic
#import hostServer

# Pygame 초기화
pygame.init()

# 창 크기 설정
window_width, window_height = 800, 600
window_surface = pygame.display.set_mode((window_width, window_height))

# 선택 변수
selected_option = None

# 방 창 생성 함수
def create_room():
    global ip_address
    # 서버 열기
    lobbyforServer.lobby()
    #server.open_server()
    print("방이 생성되었습니다.")
    
    # IP 주소 가져오기
    #ip_address = game_logic.get_ip_address()
    # 방 생성 로직 작성
    # 서버 설정, IP 주소 등
    #hostServer
    # 예시로 방 번호 출력
    print("방이 생성되었습니다.")

# 버튼 클래스
class Button:
    def __init__(self, text, rect):
        self.rect = pygame.Rect(rect)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        font = pygame.font.SysFont('comicsansms', 50)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# 버튼 생성
button_width = 200
button_height = 50
button_x = window_width // 2 - button_width // 2
button_y = window_height // 2 - button_height // 2

host_button_rect = pygame.Rect(button_x, button_y - button_height, button_width, button_height)
user_button_rect = pygame.Rect(button_x, button_y + button_height, button_width, button_height)

host_button = Button("HOST", host_button_rect)
user_button = Button("USER", user_button_rect)

def run():
    global selected_option
    # 이벤트 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if host_button.is_clicked(pos):
                    selected_option = "host"
                elif user_button.is_clicked(pos):
                    selected_option = "user"

        # 배경 그리기
        window_surface.fill((255, 255, 255))

        # 버튼 그리기
        host_button.draw(window_surface)
        user_button.draw(window_surface)

        # 선택된 옵션에 따라 동작 수행
        if selected_option == "host":
            create_room()
            running = False
        elif selected_option == "user":
            # IP 주소 입력 받기
            ipAdressInput2.run_client()
            # ip_address = input("방장의 IP 주소를 입력하세요: ")
            # join_room(ip_address)
            # running = False

        pygame.display.update()

    # Pygame 종료
    pygame.quit()


if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))
    run()
