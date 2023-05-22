import pygame
import pygame_gui
#import hostServer

# # 유저 창 생성 함수
# def join_room(ip_address):
#     # 유저 참가 로직 작성
#     # 클라이언트 설정, IP 주소 등
#     if ip_address == hostServer.SERVER_IP:
#         # 예시로 IP 주소 출력
#         print("방에 참가하였습니다. IP 주소:", ip_address)
#     else:
#         print("잘못된 IP 주소입니다.")

def display_message(window_surface, font, message, position):
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=position)
    window_surface.blit(text, text_rect)

def run_client():
    pygame.init()
    clock = pygame.time.Clock()

    # 화면 크기 설정
    window_width, window_height = 800, 600
    window_surface = pygame.display.set_mode((window_width, window_height))

    # 팝업 관리자 생성
    manager = pygame_gui.UIManager((window_width, window_height))

    # IP 입력 창 생성
    input_box = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 200), (200, 30)),
                                                    manager=manager)

    # 버튼 생성
    join_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 250), (100, 30)),
                                            text='Join',
                                            manager=manager)
    
    # 이벤트 루프
    running = True
    display_ip_message = False
    ip_message_timer = 0
    ip_message_duration = 3  # IP 주소 메시지 표시 시간 (초)

    while running:
        time_delta = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == join_button:
                        ip_address = input_box.text
                        #join_room(ip_address)  # join_room 함수 호출
                        pass
                        display_ip_message = True
                        ip_message_timer = pygame.time.get_ticks()  # IP 주소 메시지 표시 타이머 시작

            manager.process_events(event)

        manager.update(time_delta)
        
        window_surface.fill((255, 255, 255))
        manager.draw_ui(window_surface)

        if display_ip_message:
            font = pygame.font.Font(None, 30)
            position = (window_width // 2, window_height // 2)
            display_message(window_surface, font, f"IP 주소: {input_box.text}", position)

            current_time = pygame.time.get_ticks()
            if current_time - ip_message_timer >= ip_message_duration * 1000:
                display_ip_message = False

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))
    run_client()
