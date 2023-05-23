import pygame

pygame.init()

# 화면 크기와 배경색 설정
screen_size1 = (800, 600)
screen_size2 = (1600, 800)

background_color = (255, 255, 255)  # 흰색

# 화면 생성
screen = pygame.display.set_mode(screen_size1)

# 배경색 설정
screen.fill(background_color)

# 화면 업데이트
pygame.display.flip()

# 버튼 생성 함수
def create_button(text, x, y, width, height, inactive_color, active_color, action=None):
    # 색상 정의
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    font = pygame.font.SysFont(None, 40)

    # 버튼 텍스트 생성
    button_text = font.render(text, True, BLACK)
    text_rect = button_text.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)

    # 버튼 바탕 생성
    button_rect = pygame.Rect(x, y, width, height)

    # 마우스 오버 시 색상 변경
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, active_color, button_rect)
    else:
        pygame.draw.rect(screen, inactive_color, button_rect)

    # 버튼 텍스트 그리기
    screen.blit(button_text, text_rect)

    # 클릭 시 액션 실행
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0] == 1 and button_rect.collidepoint(mouse_pos):
        if action is not None:
            action()

# 게임 루프
while True:
    for event in pygame.event.get():
        # 게임 종료 이벤트 처리
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



        # 키 이벤트 처리-> 버튼으로 바꾸지
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_F11:
                # 전체 화면 모드
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            elif event.key == pygame.K_F9:
                # 윈도우 모드
                screen = pygame.display.set_mode(screen_size1)

            elif event.key == pygame.K_F10:
                # 윈도우 모드
                screen = pygame.display.set_mode(screen_size2)

            elif event.key == pygame.K_ESCAPE:

                # 윈도우 모드
                screen = pygame.display.set_mode(screen_size1)
            elif event.key == pygame.K_q:
                # 게임 종료
                pygame.quit()
                exit()


    # 화면 업데이트
    pygame.display.flip()
